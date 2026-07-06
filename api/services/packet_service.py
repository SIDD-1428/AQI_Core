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
    
    def get_nodes(self):
        return self.manager.get_nodes()
    
    def get_latest_node(self,node):
        return self.manager.get_latest_node(node)
    
    def get_history_by_node(self,node_id,limit):
        return self.manager.get_history_by_node(node_id,limit)
    
    def close(self):
        self.manager.close()
        self.session.close()