from database.engine import SessionLocal
from database.manager import DatabaseManager
from database.aqi_result_manager import AQIResultManager
from datetime import datetime,timezone

class PacketService:
    def __init__(self):
        self.session=SessionLocal()
        self.manager=DatabaseManager()
        self.aqi_manager=AQIResultManager(self.session)

    def get_latest_packet(self):
        return self.manager.get_latest_packet()
    
    def get_history(self,limit=50):
        return self.manager.get_all_packets(limit)
    
    def get_nodes(self):
        return self.manager.get_nodes()
    
    def get_node_summary(self):
        packets=self.manager.get_node_summary()
        nodes=[]
        for packet in packets:
            latest_aqi=self.aqi_manager.get_latest_by_node(packet.node)
            seconds=(datetime.now(timezone.utc)-packet.received_at.replace(tzinfo=timezone.utc)).total_seconds()
            nodes.append({
                "node":packet.node,
                "status":"online"
                if seconds <= 15
                else "offline",
                "last_seen":packet.received_at,
                "temperature":packet.temperature,
                "humidity":packet.humidity,
                "aqi":latest_aqi.aqi
                if latest_aqi
                else 0,
                "rssi":packet.rssi,
                "snr":packet.snr,
            })
        return nodes
    
    def get_latest_node(self,node):
        return self.manager.get_latest_node(node)
    
    def get_history_by_node(self,node_id,limit):
        return self.manager.get_history_by_node(node_id,limit)
    
    def close(self):
        self.manager.close()
        self.session.close()