from typing import Any

from .context import PostProcessingContext

from .detectors.anomaly_detector import AnomalyDetector
from .observation.observation_manager import ObservationManager
from .observation.observation_processor import ObservationProcessor
from .filters.filtered_packet_builder import FilteredPacketBuilder
from .validators.aqi_validator import AQIValidator
from aqi.engine import AQIEngine


class PostProcessingEngine:

    """Coordinates anomaly detection, observation and filtering."""

    def __init__(self, aqi_engine:AQIEngine):

        self._anomaly_detector = AnomalyDetector()
        self._observation_manager = ObservationManager()
        self._observation_processor = ObservationProcessor()
        self._filtered_packet_builder = FilteredPacketBuilder()
        self._aqi_validator = AQIValidator (aqi_engine)

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
            context.final_result_available = True
            context.current_stage="ACCEPTED"

            return context

        # 4. Start observations for detected anomalies
        context.anomaly_detected = True
        context.observation_required = True
        context.final_result_available=False

        for result in anomalies:
            if result.signal is None:
                continue

            # Do not start another observation for a signal
            # that is already being observed.
            if self._observation_manager.is_observing(result.signal):
                continue

            self._observation_manager.start_observation(
                signal=result.signal,
                reason=result.reason,
                trigger_packet=packet
            )

            observation_window = (
                self._observation_manager.get_window(result.signal)
            )

            if observation_window is not None:
                observation_window.add_packet(packet)

                context.observation_packets_collected = (
                    observation_window.collected()
                )

                context.observation_window_size = (
                    observation_window.window_size
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

        if filtered_signals:

            trigger_packet = None

            for window in completed_windows:

                if window.trigger_packet is not None:
                    trigger_packet = window.trigger_packet
                    break

            base_packet = (
                trigger_packet
                if trigger_packet is not None
                else context.packet
            )

            context.result_packet = base_packet

            context.filtered_packet = (
                self._filtered_packet_builder.build(
                    packet=base_packet,
                    filtered_signals=filtered_signals
                )
            )

            post_processed_aqi = (
                self._aqi_validator.validate(
                    packet=context.filtered_packet,
                    context=context
                )
            )

            context.report = post_processed_aqi
            context.final_result_available = True
            context.accepted = True
            context.rejected = False
            context.observation_complete = True

            context.metadata[
                "filtered_signals"
            ] = filtered_signals

            context.current_stage = "AQI_VALIDATED"

        self._observation_manager.clear_completed()