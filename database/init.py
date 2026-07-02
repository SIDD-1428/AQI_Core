from database.engine import Base
from database.engine import engine

import database.models

def initialize_database():
    Base.metadata.create_all(bind=engine)
    print("Database initialized successfully")

if __name__ == "__main__":
    initialize_database()