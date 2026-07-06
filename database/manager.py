from database.engine import SessionLocal
from database.models import Packet
from database.repository import EnvironmentalRepository

class DatabaseManager:
    def __init__(self):
        self.session=SessionLocal()
        self.repositiory=EnvironmentalRepository(self.session)

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
        return self.repositiory.save(data)
        
    
    def get_latest_packet(self):
        return self.repositiory.get_latest()
    
    def get_all_packets(self,limit):
        return self.repositiory.get_latest(limit)
    
    def get_nodes(self):
        return self.repositiory.get_nodes()
    
    def get_latest_node(self,node):
        return self.repositiory.get_latest_by_node(node)
    
    def get_history_by_node(self,node, limit):
        return self.repositiory.get_history_by_node(node,limit)
    
    def close(self):
        self.session.close()