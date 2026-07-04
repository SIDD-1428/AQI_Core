from database.engine import Base
from database.engine import engine


import database.models
import configuration.models
import configuration.breakpoint_models
import configuration.standard_models
from database.aqi_result_models import AQIResultModel

def initialize_database():
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully")

if __name__ == "__main__":
    initialize_database()