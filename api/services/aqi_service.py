from database.engine import SessionLocal
from database.aqi_result_manager import AQIResultManager

class AQIService:
    def __init__(self):
        self.session=SessionLocal()
        self.manager=AQIResultManager(self.session)

    def get_latest_aqi(self):
        return self.manager.get_latest_result()
    
    def get_history(self,limit=50):
        return self.manager.get_all_results(limit)
    
    def close(self):
        self.session.close()