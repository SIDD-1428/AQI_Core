from pydantic import BaseModel

class SystemStatusResponse(BaseModel):
    status:str
    database:str
    version:str
    packets:str
    aqi_records:int