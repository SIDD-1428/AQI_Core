from dataclasses import dataclass, field
from typing import Any

from models.packet import Packet
from parser.report import ProcessingReport

@dataclass
class ProcessingContext:
    #original packet
    raw_packet: str
    
    #parsed packet
    packet: Packet | None=None
    
    #pipeline state
    is_valid: bool = True
    
    #informational messages
    warnings: list[str]=field(default_factory=list)

    #validation/ processing errors
    errors: list[str]=field(default_factory=list)

    metadata: dict[str,Any]=field(default_factory=dict)
    quality_score: int =100

    report: ProcessingReport | None= None