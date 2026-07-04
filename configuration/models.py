from sqlalchemy import Column 
from sqlalchemy import Integer
from sqlalchemy import String
from database.engine import Base

class SystemSetting(Base):
    __tablename__="system_settings"
    id=Column(Integer, primary_key=True, index=True)
    key=Column(String, unique=True, nullable=False)
    value=Column(String, nullable=False)

    datatype=Column(String, nullable=False)
    description=Column(String)
