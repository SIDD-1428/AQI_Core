from dataclasses import dataclass

@dataclass (frozen=True)
class DetectionResult:
    """This is the result returned by every detector"""
    detected:bool
    signal:str|None=None
    reason:str=""
    confidence:float=0.0
    
    