from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from database.engine import Base

class AQIStandard(Base):

    __tablename__ = "aqi_standards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    version = Column(String, nullable=False)
    country = Column(String, nullable=False)
    active = Column(Boolean, default=False)