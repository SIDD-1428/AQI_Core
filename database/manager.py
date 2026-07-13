from database.engine import SessionLocal
from database.models import Packet
from database.repository import EnvironmentalRepository

class DatabaseManager:
    def __init__(self):
        self.session=SessionLocal()
        self.repository=EnvironmentalRepository(self.session)

    def save_packet(self,packet):
        data=Packet(
            version=packet.version,
            node=packet.node,
            sequence=packet.sequence,
            temperature=packet.temperature,
            humidity=packet.humidity,
            pressure=packet.pressure,
            pm1_0=packet.pm1_0,
            pm2_5=packet.pm2_5,
            pm10=packet.pm10,
            o3=packet.o3,
            no2=packet.no2,
            co=packet.co,
            nh3=packet.nh3,
            so2=packet.so2,
            rssi=packet.rssi,
            snr=packet.snr,
            checksum=packet.checksum,
            valid=packet.valid,
            timestamp=packet.timestamp
        )
        return self.repository.save(data)
        
    
    def get_latest_packet(self):
        return self.repository.get_latest()
    
    def get_all_packets(self,limit):
        return self.repository.get_all(limit)
    
    def get_nodes(self):
        return self.repository.get_nodes()
    
    def get_latest_node(self,node):
        return self.repository.get_latest_node(node)
    
    def get_node_summary(self):
        return self.repository.get_node_summary()
    
    def get_history_by_node(self,node_id, limit):
        return self.repository.get_history_by_node(node_id,limit)
    
    def close(self):
        self.session.close()