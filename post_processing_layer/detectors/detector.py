from abc import ABC, abstractmethod
from post_processing_layer.context import PostProcessingContext
from .detection_result import DetectionResult

class Detector(ABC):
    """This acts as a base interface for all post-processing detectors"""
    @abstractmethod
    def detect(
        self,
        context: PostProcessingContext
    )-> DetectionResult:
        """Analyyze the current context and return a detection result"""
        raise NotImplementedError

    def calculate_percentage_change(current: float, previous:float)->float:
        ...