from post_processing_layer.context import PostProcessingContext

from .detector import Detector
from .detection_result import DetectionResult

from ..config.detector_config import (
    DRIFT_THRESHOLDS,
    DRIFT_WINDOW_SIZE,
    DRIFT_MIN_TREND_RATIO,
)



class DriftDetector(Detector):

    """Detects persistent gradual movement in monitored signals."""

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

        for signal, threshold in DRIFT_THRESHOLDS.items():

            current_value = getattr(
                packet,
                signal,
                None
            )

            if current_value is None:
                continue

            values = history.get_signal_history(
                signal,
                count=DRIFT_WINDOW_SIZE
            )

            if len(values) < DRIFT_WINDOW_SIZE:
                continue

            first_value = values[0]

            if first_value == 0:
                continue

            percentage_change = (
                (current_value - first_value)
                / abs(first_value)
            ) * 100

            # Determine the overall direction
            direction = 1 if current_value > first_value else -1

            movements = len(values) - 1

            if movements == 0:
                continue

            supporting_movements = 0

            for index in range(1, len(values)):

                previous = values[index - 1]
                current = values[index]

                if direction == 1 and current > previous:
                    supporting_movements += 1

                elif direction == -1 and current < previous:
                    supporting_movements += 1

            trend_ratio = supporting_movements / movements

            if trend_ratio < DRIFT_MIN_TREND_RATIO:
                continue

            if abs(percentage_change) >= threshold:

                confidence = min(
                    abs(percentage_change) / threshold / 2,
                    1.0
                )

                return DetectionResult(
                    detected=True,
                    signal=signal,
                    reason=(
                        f"{signal} shows persistent drift of "
                        f"{percentage_change:.2f}% "
                        f"across {DRIFT_WINDOW_SIZE} observations"
                        f"(trend ratio: {trend_ratio:.2f})"
                    ),
                    confidence=round(confidence, 2)
                )

        return DetectionResult(
            detected=False,
            reason="No persistent drift detected"
        )