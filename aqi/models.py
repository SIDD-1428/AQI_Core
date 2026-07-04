from dataclasses import dataclass
from typing import Dict

@dataclass
class AQIResult:
    aqi:int
    category:str
    color:str
    dominant_pollutant:str
    subindices: Dict[str,int]