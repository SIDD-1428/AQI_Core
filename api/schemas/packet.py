from pydantic import BaseModel

class PacketResponse(BaseModel):
    node:str
    sequence:str
    temperature:float
    humidity:float
    pressure:float
    pm1_0:float
    pm2_5:float
    pm10:float
    o3:float
    no2:float
    co:float
    nh3:float
    so2:float
    rssi:float
    snr:float
    timestamp:int