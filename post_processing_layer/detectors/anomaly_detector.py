from post_processing_layer.context import PostProcessingContext

from .detection_result import DetectionResult
from .spike_detector import SpikeDetector
from .drift_detector import DriftDetector
from .stagnation_detector import StagnationDetector


class AnomalyDetector:

    """Coordinates all post-processing anomaly detectors."""

    def __init__(self):
        self._detectors = [
            SpikeDetector(),
            DriftDetector(),
            StagnationDetector(),
        ]


    def detect(
        self,
        context: PostProcessingContext
    ) -> list[DetectionResult]:

        results: list[DetectionResult] = []

        for detector in self._detectors:
            result = detector.detect(context)
            results.append(result)
        return results


    def detect_anomalies(
        self,
        context: PostProcessingContext
    ) -> list[DetectionResult]:

        results = self.detect(context)
        return [
            result
            for result in results
            if result.detected
        ]