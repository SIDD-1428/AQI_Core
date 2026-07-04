from database.models import EnvironmentalData

class EnvironmentalRepository:
    def __init__(self, session):
        self.session=session
    
    def save(self,data):
        self.session.add(data)
        self.session.commit()

    def get_latest(self):
        return(
            self.session.query(EnvironmentalData).order_by(EnvironmentalData.id.desc()).first()
        )