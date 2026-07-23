from parser.entry_point.context import ProcessingContext

class PacketNormalizer:
    """Stage 5 of processing pipeline (Normalization)"""
    FLOAT_FIELDS=(
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
        "snr",
    )

    def process(self,contex:ProcessingContext)-> ProcessingContext:
        packet=context.packet

        if packet is None:
            return context
        
        packet.node=packet.node.strip().upper()
        for field in self.FLOAT_FIELDS:
            value=getattr(packet,field)
            setattr(packet,field,round(float(value),2))
        
        packet.rssi=int(packet.rssi)
        context.metadata["normalization"]={
            "status":"completed"
        }

        return context