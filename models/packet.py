from dataclasses import dataclass

@dataclass
class Packet:
    version: int
    node:str
    sequence:int

    #climate
    temperature:float
    humidity:float
    pressure:float

    #particulates
    pm1_0:float
    pm2_5:float
    pm10:float

    #gas
    o3:float
    no2:float
    co:float
    nh3:float
    so2:float

    #radio
    rssi:float
    snr:float

    #validation
    checksum:int
    valid:bool
    timestamp:int
