from typing import Any

from post_processing_layer.context import PostProcessingContext

from .detector import Detector
from .detection_result import DetectionResult

from ..config.detector_config import SPIKE_THRESHOLDS


class SpikeDetector(Detector):

    """Detects sudden abnormal changes in monitored signals."""

    def detect(
        self,
        context: PostProcessingContext
    ) -> DetectionResult:

        packet = context.packet
        history = context.history

        if packet is None:
            return DetectionResult(
                detected=False,
                reason="No packet available"
            )

        if history is None:
            return DetectionResult(
                detected=False,
                reason="No history manager available"
            )

        for signal, threshold in SPIKE_THRESHOLDS.items():

            current_value = getattr(
                packet,
                signal,
                None
            )

            if current_value is None:
                continue

            previous_values = history.get_signal_history(
                signal,
                count=10
            )

            if not previous_values:
                continue

            baseline = sum(previous_values) / len(previous_values)

            if baseline == 0:
                continue

            percentage_change = (
                abs(current_value - baseline)
                / abs(baseline)
            ) * 100

            if percentage_change >= threshold:

                confidence = min(
                    percentage_change / threshold / 2,
                    1.0
                )

                return DetectionResult(
                    detected=True,
                    signal=signal,
                    reason=(
                        f"{signal} changed by "
                        f"{percentage_change:.2f}% "
                        f"from historical baseline "
                        f"{baseline:.2f}%"
                    ),
                    confidence=round(confidence, 2)
                )

        return DetectionResult(
            detected=False,
            reason="No abnormal spike detected"
        )