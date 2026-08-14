from typing import Any

from .context import PostProcessingContext

from .detectors.anomaly_detector import AnomalyDetector
from .observation.observation_manager import ObservationManager
from .observation.observation_processor import ObservationProcessor
from .filters.filtered_packet_builder import FilteredPacketBuilder

class PostProcessingEngine:

    """Coordinates anomaly detection, observation and filtering."""

    def __init__(self):

        self._anomaly_detector = AnomalyDetector()
        self._observation_manager = ObservationManager()
        self._observation_processor = ObservationProcessor()
        self._filtered_packet_builder = FilteredPacketBuilder()

    def process(
        self,
        packet: Any,
        history: Any
    ) -> PostProcessingContext:

        context = PostProcessingContext(
            packet=packet,
            history=history
        )

        context.current_stage = "DETECTION"

        # 1. Feed packet into existing observations
        self._observation_manager.process_packet(packet)


        # 2. Process any observations that completed
        self._process_completed_observations(context)

        # 3 Detect new anomalies
        detection_results = self._anomaly_detector.detect(
            context
        )

        anomalies = [
            result
            for result in detection_results
            if result.detected
        ]

        if not anomalies:
            context.accepted = True
            context.filtered_packet = packet
            context.current_stage = "ACCEPTED"

            return context

        # 4. Start observations for detected anomalies
        context.anomaly_detected = True
        context.observation_required = True

        for result in anomalies:
            if result.signal is None:
                continue

            self._observation_manager.start_observation(
                signal=result.signal,
                reason=result.reason
            )

            # The packet that triggered the anomaly
            # becomes observation #1.
            observation_window = (
                self._observation_manager
                .get_window(result.signal)
            )

            if observation_window is not None:
                observation_window.add_packet(packet)
                context.observation_packets_collected = (
                    observation_window.collected()
                )

            context.observation_started = True
            context.warnings.append(
                f"Observation started for {result.signal}: "
                f"{result.reason}"
            )
        context.current_stage = "OBSERVING"

        return context


    def _process_completed_observations(
        self,
        context: PostProcessingContext
    ) -> None:

        completed_windows = (
            self._observation_manager
            .get_completed_windows()
        )

        if not completed_windows:
            return

        context.current_stage = "FILTERING"

        filtered_signals: dict[str, float] = {}

        for window in completed_windows:

            packets = window.get_packets()

            if not packets:
                continue

            # The latest packet in the completed
            # observation window is the packet that
            # completed the observation.
            latest_observation_packet = packets[-1]

            original_value = getattr(
                latest_observation_packet,
                window.signal,
                None
            )

            result = self._observation_processor.process(
                window=window,
                original_value=original_value
            )

            if not result.success:

                context.warnings.append(
                    f"Filtering failed for "
                    f"{window.signal}: "
                    f"{result.reason}"
                )

                continue

            if result.filtered_value is None:
                continue

            filtered_signals[window.signal] = (
                result.filtered_value
            )

            context.confidence = max(
                context.confidence,
                result.confidence
            )

            context.filter_applied = True

        # Build a completely separate filtered packet.
        if filtered_signals:

            context.filtered_packet = (
                self._filtered_packet_builder.build(
                    packet=context.packet,
                    filtered_signals=filtered_signals
                )
            )

            context.metadata[
                "filtered_signals"
            ] = filtered_signals

            context.current_stage = "FILTERED"

        self._observation_manager.clear_completed()