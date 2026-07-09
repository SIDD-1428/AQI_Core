from pydantic import BaseModel

class SystemStatusResponse(BaseModel):
    status:str
    database:str
    version:str
    packets:int
    aqi_records:int