from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship
from database.models import Packet
from datetime import datetime
from database.engine import Base

class AQIResultModel(Base):
    __tablename__="aqi_results"
    id=Column(Integer,primary_key=True, index=True)

    packet_id=Column(Integer,ForeignKey("packets.id"),nullable=False)
    node = Column(String, nullable=False)
    aqi = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    dominant_pollutant = Column(String, nullable=False)
    pm2_5_index = Column(Integer)
    pm10_index = Column(Integer)
    no2_index = Column(Integer)
    so2_index = Column(Integer)
    co_index = Column(Integer)
    o3_index = Column(Integer)
    nh3_index = Column(Integer)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
    packet = relationship(Packet)
