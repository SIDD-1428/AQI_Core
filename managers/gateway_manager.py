from communication.serial_listener import SerialListener
from parser.packet_processor import PacketProcessor
from database.manager import DatabaseManager

from database.engine import SessionLocal
from configuration.breakpoint_manager import BreakpointManager
from configuration.standard_manager import StandardManager
from aqi.engine import AQIEngine

class GatewayManager:
    def __init__(self):
        self.listener=SerialListener()
        self.database=DatabaseManager()
        self.session=SessionLocal()
        self.breakpoint_manager=BreakpointManager(self.session)
        self.standard_manager=StandardManager(self.session)

        self.aqi_engine=AQIEngine(
            self.breakpoint_manager,
            self.standard_manager
        )
    
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
            aqi_result=self.aqi_engine.calculate(packet)
            self.handle_packet(packet, aqi_result)

    
    def handle_packet(self, packet, aqi_result):
        print("--------------------------------")        
        try:
            self.database.save_packet(packet)
        except Exception as e:
            print(f"Database Error: {e}")
            return
        
        print("\n==================================================")
        print(f"Packet Received  |  Node : {packet.node}")
        print("==================================================")

        print("\nRAW SENSOR DATA")
        print("----------------------------------------")
        print(f"Sequence     : {packet.sequence}")
        print(f"Temperature  : {packet.temperature:.2f} °C")
        print(f"Humidity     : {packet.humidity:.2f} %")
        print(f"Pressure     : {packet.pressure:.2f} hPa")
        print(f"CO           : {packet.co:.2f} ppm")

        # Uncomment these when the sensors are connected
        # print(f"PM2.5        : {packet.pm2_5:.2f} µg/m³")
        # print(f"PM10         : {packet.pm10:.2f} µg/m³")
        # print(f"NO2          : {packet.no2:.2f} µg/m³")
        # print(f"SO2          : {packet.so2:.2f} µg/m³")
        # print(f"O3           : {packet.o3:.2f} µg/m³")
        # print(f"NH3          : {packet.nh3:.2f} µg/m³")
        
        print("\n--------------------------------")
        print("AQI RESULT")
        print("--------------------------------")
        print(f"AQI                 : {aqi_result.aqi}")
        print(f"Category            : {aqi_result.category}")
        print(f"Dominant Pollutant  : {aqi_result.dominant_pollutant}")
        print("\nSub-indices")
        for pollutant, value in aqi_result.subindices.items():
            print(f"{pollutant:<8}: {value}")
        print("\nCOMMUNICATION")
        print("----------------------------------------")
        print(f"RSSI         : {packet.rssi:.1f} dBm")
        print(f"SNR          : {packet.snr:.2f} dB")

        print("\nDATABASE")
        print("----------------------------------------")
        print("✓ Packet saved successfully")

        print("==================================================\n")