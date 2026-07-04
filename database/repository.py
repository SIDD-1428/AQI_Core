from database.models import Packet

class EnvironmentalRepository:
    def __init__(self, session):
        self.session=session
    
    def save(self,data):
        self.session.add(data)
        self.session.commit()
        self.session.refresh(data)
        return data

    def get_latest(self):
        return(
            self.session.query(Packet).order_by(Packet.id.desc()).first()
        )