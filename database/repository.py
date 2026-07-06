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
    
    def get_all(self,limit):
        return(
            self.session.query(Packet)
            .order_by(Packet.id.desc())
            .limit(limit)
            .all()
        )
    
    def get_nodes(self):
        return(
            self.session.query(Packet.node)
            .distinct()
            .all()
        )
    
    def get_latest_node(self,node):
        return(
            self.session.query(Packet)
            .filter(Packet.node==node)
            .order_by(Packet.id.desc())
            .first()
        )
    
    def get_history_by_node(self,node_id,limit):
        return(
            self.session.query(Packet)
            .filter(Packet.node==node_id)
            .order_by(Packet.id.desc())
            .limit(limit)
            .all()
        )