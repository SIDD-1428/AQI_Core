from post_processing_layer.context import PostProcessingContext
from post_processing_layer.config import (
    MONITORED_SIGNALS,
    SPIKE_THRESHOLDS,
)
from detector import Detector
from .detection_result import DetectionResult

class SpikeDetector(Detector):
    """Detects sudden spikes in the sensor values"""
    def detect(self,context: PostProcessingContext)-> DetectionResult:
        ...