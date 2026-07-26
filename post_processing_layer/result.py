from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class PostProcessingResult:
    #final
    packet:Any

    #Decision
    accepted:bool
    filter_applied:bool

    #Metrics
    confidence:float
    stability_score:float

    #observation
    observation_used:bool
    observation_window:bool

    #diagnostics
    remarks: str=""