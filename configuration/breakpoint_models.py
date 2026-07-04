#tablecreation of breakpoints
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from database.engine import Base


class AQIBreakpoint(Base):
    __tablename__ = "aqi_breakpoints"
    id = Column(Integer, primary_key=True, index=True)
    pollutant = Column(String, nullable=False)

    standard_id = Column(
        Integer,
        ForeignKey("aqi_standards.id"),
        nullable=False
    )

    aqi_low = Column(Integer, nullable=False)
    aqi_high = Column(Integer, nullable=False)
    conc_low = Column(Float, nullable=False)
    conc_high = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    color = Column(String, nullable=False)
    health_message = Column(String)
    standard = relationship("AQIStandard")
