from datetime import datetime

from pydantic import BaseModel


class AQISubindices(BaseModel):
    PM2_5: int | None = None
    PM10: int | None = None
    NO2: int | None = None
    SO2: int | None = None
    CO: int | None = None
    O3: int | None = None
    NH3: int | None = None


class AQIResponse(BaseModel):
    aqi: int
    category: str
    dominant_pollutant: str
    created_at: datetime
    subindices: AQISubindices
