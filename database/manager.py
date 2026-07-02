from database.engine import SessionLocal
from database.models import EnvironmentalData

class DatabaseManager:
    def __init__(self):
        self.session=SessionLocal()
    
    def save_packet(self,packet):
        data=EnvironmentalData(
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

        self.session.add(data)
        self.session.commit()
    
    def close(self):
        self.session.close()