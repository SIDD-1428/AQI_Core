from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL="sqlite:///aqi_core.db"

#engine
engine=create_engine(DATABASE_URL, echo=False)

Base=declarative_base()

#session factory
SessionLocal=sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)