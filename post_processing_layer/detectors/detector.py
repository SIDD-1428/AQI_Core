from abc import ABC, abstractmethod

from post_processing_layer.context import PostProcessingContext

from .detection_result import DetectionResult


class Detector(ABC):

    """This acts as a base interface for all post-processing detectors."""

    @abstractmethod
    def detect(
        self,
        context: PostProcessingContext
    ) -> DetectionResult:
        """Analyze the current context and return a detection result."""
        raise NotImplementedError


    @staticmethod
    def calculate_percentage_change(
        current: float,
        previous: float
    ) -> float:

        if previous == 0:
            return 0.0

        return ((current - previous) / abs(previous)) * 100