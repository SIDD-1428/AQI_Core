from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import Boolean

from database.engine import Base

class EnvironmentalData(Base):
    __tablename__="packets"

    #pk
    id=Column(Integer,primary_key=True, index=True)

    version =Column(Integer)
    node=Column(String)
    sequence=Column(Integer)
    temperature=Column(Float)
    humidity=Column(Float)
    pressure=Column(Float)
    pm1_0=Column(Float)
    pm2_5=Column(Float)
    pm10=Column(Float)
    o3=Column(Float)
    no2=Column(Float)
    co=Column(Float)
    nh3=Column(Float)
    so2=Column(Float)
    rssi=Column(Float)
    snr=Column(Float)
    checksum=Column(Integer)
    valid=Column(Boolean)
    timestamp=Column(Integer)
