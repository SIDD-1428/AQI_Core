from database.engine import SessionLocal
from database.manager import DatabaseManager

class PacketService:
    def __init__(self):
        self.session=SessionLocal()
        self.manager=DatabaseManager()

    def get_latest_packet(self):
        return self.manager.get_latest_packet()
    
    def get_history(self,limit=50):
        return self.manager.get_all_packets(limit)
    
    def close(self):
        self.manager.close()
        self.session.close()