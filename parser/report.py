from dataclasses import dataclass, field
from typing import Any

@dataclass
class ProcessingReport:
    success:bool
    processing_time_ms:float
    quality_score:int
    grade:str
    status:str
    stages:dict[str,str]=field(default_factory=dict)
    warnings:list[dict[str,Any]]=field(default_factory=list)
    errors:list[dict[str,Any]]=field(default_factory=list)
    metadata:dict[str,Any]=field(default_factory=dict)