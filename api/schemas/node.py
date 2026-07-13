from datetime import datetime
from pydantic import BaseModel

class NodeSummary(BaseModel):
    node: str
    status: str
    last_seen: datetime
    temperature: float
    humidity: float
    aqi: int
    rssi: float
    snr: float

class NodeListResponse(BaseModel):
    nodes: list[NodeSummary]