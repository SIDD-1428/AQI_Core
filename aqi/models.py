from dataclasses import dataclass

@dataclass
class AQIResult:
    aqi:int
    category:str
    color:str
    dominant_pollutant:str