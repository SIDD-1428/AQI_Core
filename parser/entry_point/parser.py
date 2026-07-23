import json
from models.packet import Packet
from parser.entry_point.context import ProcessingContext
from parser.dataclass.exceptions import PacketParserError

class PacketParser:
    REQUIRED_FIELDS=[
        "version",
        "node",
        "sequence",
        "temperature",
        "humidity",
        "pressure",
        "pm1_0",
        "pm2_5",
        "pm10",
        "o3",
        "no2",
        "co",
        "nh3",
        "so2",
        "rssi",
        "snr",
        "checksum",
        "valid",
        "timestamp",
    ]

    def process(self,context:ProcessingContext)-> ProcessingContext:
        try:
            data=json.loads(context.raw_packet)
        
        except json.JSONDecodeError as e:
            raise PacketParserError(f"Invalid JSON packet: {e.msg}")
        missing_fields=[
            field for field in self.REQUIRED_FIELDS
            if field not in data
        ]

        if missing_fields:
            raise PacketParserError(
            f"Missing required fields: {','.join(missing_fields)}"
            )
            
        context.packet=Packet(
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
        context.metadata["parser"]="success"
        return context