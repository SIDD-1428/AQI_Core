import json
from models.packet import Packet

class PacketProcessor:

    @staticmethod
    def process(raw_packet: str)-> Packet:
        data=json.loads(raw_packet)

        return Packet(
            version=data["version"],
            node=data["node"],
            sequence=data["sequence"],
            temperature=data["temperature"],
            humidity=data["humidity"],
            pressure=data["pressure"],
            pm1_0=data["pm1_0"],
            pm2_5=data["pm2_5"],
            pm10=data["pm10"],
            o3=data["o3"],
            no2=data["no2"],
            co=data["co"],
            nh3=data["nh3"],
            so2=data["so2"],
            rssi=data["rssi"],
            snr=data["snr"],
            checksum=data["checksum"],
            valid=data["valid"],
            timestamp=data["timestamp"]
        )