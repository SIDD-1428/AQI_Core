from database.aqi_result_repository import AQIResultRepository

class AQIResultManager:
    def __init__(self,session):
        self.repository=AQIResultRepository(session)
    
    def save_result(self,result):
        self.repository.save(result)
    
    def get_latest_result(self):
        return self.repository.latest()
    
    def get_all_results(self):
        return self.repository.get_all()