from post_processing_layer.context import PostProcessingContext

from .detector import Detector
from .detection_result import DetectionResult

from ..config.detector_config import (
    STAGNATION_LIMITS,
    STAGNATION_TOLERANCE,
)


class StagnationDetector(Detector):

    """Detects signals that remain effectively unchanged for too long."""

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

        for signal, limit in STAGNATION_LIMITS.items():

            current_value = getattr(
                packet,
                signal,
                None
            )

            if current_value is None:
                continue

            values = history.get_signal_history(
                signal,
                count=limit
            )

            if len(values) < limit:
                continue

            reference_value = values[0]

            stagnant = True

            for value in values[1:]:

                difference = abs(
                    value - reference_value
                )

                if difference > STAGNATION_TOLERANCE:
                    stagnant = False
                    break

            if not stagnant:
                continue

            return DetectionResult(
                detected=True,
                signal=signal,
                reason=(
                    f"{signal} remained effectively unchanged "
                    f"for {limit} observations"
                ),
                confidence=1.0
            )

        return DetectionResult(
            detected=False,
            reason="No stagnant signal detected"
        )