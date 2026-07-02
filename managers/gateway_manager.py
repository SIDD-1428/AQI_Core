from communication.serial_listener import SerialListener
from parser.packet_processor import PacketProcessor
from database.manager import DatabaseManager

class GatewayManager:
    def __init__(self):
        self.listener=SerialListener()
        self.database=DatabaseManager()
    
    def run(self):
        print("AQI Core Started")
        print("-----------------")

        while True:
            raw_packet=self.listener.read_line()
            if not raw_packet: 
                continue
            if not raw_packet.startswith("{"):
                continue

            packet=PacketProcessor.process(raw_packet)
            self.handle_packet(packet)

    
    def handle_packet(self, packet):
        print("--------------------------------")        
        try:
            self.database.save_packet(packet)
            print("✓ Packet saved to database")
        except Exception as e:
            print(f"Database Error: {e}")
            return
        
        print("--------------------------------")
        print(f"Node        : {packet.node}")
        print(f"Sequence    : {packet.sequence}")
        print(f"Temperature : {packet.temperature:.2f} °C")
        print(f"Humidity    : {packet.humidity:.2f} %")
        print(f"Pressure    : {packet.pressure:.2f} hPa")
        print(f"CO          : {packet.co:.2f} ppm")
        print(f"RSSI        : {packet.rssi:.1f} dBm")
        print(f"SNR         : {packet.snr:.2f} dB")
