from pydantic import BaseModel
from datetime import datetime

class SystemStatusResponse(BaseModel):
    status:str
    database:str
    version:str
    packets:int
    aqi_records:int
    last_packet:datetime|None
    last_aqi:datetime|None
    node_count:int
    uptime:str