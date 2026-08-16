from communication.serial_listener import SerialListener
from parser.packet_processor import PacketProcessor
from database.manager import DatabaseManager
from typing import Any
from database.engine import SessionLocal
from configuration.breakpoint_manager import BreakpointManager
from configuration.standard_manager import StandardManager
from aqi.engine import AQIEngine
from database.aqi_result_models import AQIResultModel
from database.aqi_result_manager import AQIResultManager
from post_processing_layer.post_processing_engine import PostProcessingEngine
from post_processing_layer.history.history_manager import HistoryManager

class GatewayManager:
    def __init__(self):
        self.listener=SerialListener()
        self.database=DatabaseManager()
        self.session=SessionLocal()
        self.breakpoint_manager=BreakpointManager(self.session)
        self.standard_manager=StandardManager(self.session)
        self.aqi_result_manager=AQIResultManager(self.session)

        self.aqi_engine=AQIEngine(
            self.breakpoint_manager,
            self.standard_manager
        )

        self.post_processing_engine = PostProcessingEngine(
            aqi_engine=self.aqi_engine
        )

        self.history_manager = HistoryManager()
        self._saved_packet_ids: dict[ Any, int]={}
    
    def run(self):
        print("AQI Core Started")
        print("-----------------")

        while True:
            raw_packet = self.listener.read_line()
            if not raw_packet:
                continue
            if not raw_packet.startswith("{"):
                continue

            packet = PacketProcessor.process(raw_packet)

            # Initial AQI calculation
            initial_aqi_result = self.aqi_engine.calculate(packet)

            # Post-processing
            context = self.post_processing_engine.process(
                packet=packet,
                history=self.history_manager
            )

            # Always save the raw packet.
            try:
                saved_packet = self.database.save_packet(packet)

                self._saved_packet_ids[
                    packet.sequence
                ] = saved_packet.id

            except Exception as e:
                print(f"Database Error while saving packet: {e}")
                continue

            # Add packet to history only AFTER post-processing.
            self.history_manager.add_packet(packet)

            # Save AQI only when a final result is available.
            if context.final_result_available:

                final_aqi_result = (
                    context.report
                    if context.report is not None
                    else initial_aqi_result
                )

                result_packet = (
                    context.result_packet
                    if context.result_packet is not None
                    else packet
                )

                result_packet_id = self._saved_packet_ids.get(
                    result_packet.sequence
                )

                if result_packet_id is None:

                    print(
                        "Database Warning: Could not find "
                        f"saved packet for sequence "
                        f"{result_packet.sequence}"
                    )

                    continue

                self.handle_packet(
                    packet=result_packet,
                    aqi_result=final_aqi_result,
                    packet_id=result_packet_id
                )

            else:

                print("--------------------------------")
                print(
                    f"Packet {packet.sequence} is under observation."
                )
                print(
                    "Final AQI will be saved after "
                    "observation is complete."
                )
    
    def handle_packet(self, packet, aqi_result,packet_id):
        print("--------------------------------")        
        try:
            aqi_record=AQIResultModel(
                packet_id=packet_id,
                node=packet.node,

                aqi=aqi_result.aqi,
                category=aqi_result.category,
                dominant_pollutant=aqi_result.dominant_pollutant,

                pm2_5_index=aqi_result.subindices["PM2_5"],
                pm10_index=aqi_result.subindices["PM10"],
                no2_index=aqi_result.subindices["NO2"],
                so2_index=aqi_result.subindices["SO2"],
                co_index=aqi_result.subindices["CO"],
                o3_index=aqi_result.subindices["O3"],
                nh3_index=aqi_result.subindices["NH3"],
            )
            self.aqi_result_manager.save_result(aqi_record)
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
        print(f"Packet ID       : {packet_id}")
        print("✓ Final AQI result saved successfully")
        print("✓ AQI result saved successfully")

        print("==================================================\n")