from pydantic import BaseModel

class AQISubindices(BaseModel):
    PM2_5:int
    PM10:int
    NO2:int
    SO2:int
    CO:int
    O3:int
    NH3:int

class AQIResponse(BaseModel):
    aqi:int
    category:str
    dominant_pollutant:str
    subindices:AQISubindices