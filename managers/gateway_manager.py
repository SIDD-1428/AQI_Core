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
        self.listener = SerialListener()
        self.database = DatabaseManager()
        self.session = SessionLocal()
        self.breakpoint_manager = BreakpointManager(self.session)
        self.standard_manager = StandardManager(self.session)
        self.aqi_result_manager = AQIResultManager(self.session)

        self.aqi_engine = AQIEngine(
            self.breakpoint_manager,
            self.standard_manager
        )

        self.post_processing_engine = PostProcessingEngine(
            aqi_engine=self.aqi_engine
        )

        self.history_manager = HistoryManager()
        # Include the node ID because sequence numbers may repeat across nodes.
        self._saved_packet_ids: dict[tuple[str, Any], int] = {}

    def run(self):
        print("AQI Core Started")
        print("-----------------")

        while True:
            raw_packet = self.listener.read_line()
            if not raw_packet or not raw_packet.startswith("{"):
                continue

            packet = PacketProcessor.process(raw_packet)

            # Calculate the initial AQI before post-processing.
            initial_aqi_result = self.aqi_engine.calculate(packet)

            context = self.post_processing_engine.process(
                packet=packet,
                history=self.history_manager
            )

            # Always preserve the raw packet, even when AQI cannot be calculated.
            try:
                saved_packet = self.database.save_packet(packet)
                packet_key = (packet.node, packet.sequence)
                self._saved_packet_ids[packet_key] = saved_packet.id

                # Observation windows are short; retain a bounded lookup so
                # long-running gateway sessions do not grow this map forever.
                while len(self._saved_packet_ids) > 256:
                    oldest_key = next(iter(self._saved_packet_ids))
                    self._saved_packet_ids.pop(oldest_key, None)
            except Exception as exc:
                print(f"Database Error while saving packet: {exc}")
                continue

            # Add packet to history only after post-processing.
            self.history_manager.add_packet(packet)

            if not context.final_result_available:
                print("--------------------------------")
                print(f"Packet {packet.sequence} is under observation.")
                print("Final AQI result is not available yet.")
                continue

            final_aqi_result = (
                context.report
                if context.report is not None
                else initial_aqi_result
            )

            if final_aqi_result is None:
                print(
                    "AQI Warning: No configured breakpoint matched "
                    f"any pollutant for node {packet.node}, "
                    f"sequence {packet.sequence}. Raw packet was saved; "
                    "no AQI result was created."
                )
                continue

            result_packet = (
                context.result_packet
                if context.result_packet is not None
                else packet
            )
            result_packet_key = (
                result_packet.node,
                result_packet.sequence
            )
            result_packet_id = self._saved_packet_ids.get(result_packet_key)

            if result_packet_id is None:
                print(
                    "Database Warning: Could not find saved packet for "
                    f"node {result_packet.node}, "
                    f"sequence {result_packet.sequence}"
                )
                continue

            self.handle_packet(
                packet=result_packet,
                aqi_result=final_aqi_result,
                packet_id=result_packet_id
            )

    def handle_packet(self, packet, aqi_result, packet_id):
        print("--------------------------------")
        try:
            subindices = aqi_result.subindices or {}
            aqi_record = AQIResultModel(
                packet_id=packet_id,
                node=packet.node,
                aqi=aqi_result.aqi,
                category=aqi_result.category,
                dominant_pollutant=aqi_result.dominant_pollutant,
                pm2_5_index=subindices.get("PM2_5"),
                pm10_index=subindices.get("PM10"),
                no2_index=subindices.get("NO2"),
                so2_index=subindices.get("SO2"),
                co_index=subindices.get("CO"),
                o3_index=subindices.get("O3"),
                nh3_index=subindices.get("NH3"),
            )
            self.aqi_result_manager.save_result(aqi_record)
        except Exception as exc:
            print(f"Database Error while saving AQI result: {exc}")
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

        print("\n--------------------------------")
        print("AQI RESULT")
        print("--------------------------------")
        print(f"AQI                 : {aqi_result.aqi}")
        print(f"Category            : {aqi_result.category}")
        print(f"Dominant Pollutant  : {aqi_result.dominant_pollutant}")
        print("\nSub-indices")
        for pollutant, value in subindices.items():
            print(f"{pollutant:<8}: {value}")

        print("\nCOMMUNICATION")
        print("----------------------------------------")
        print(f"RSSI         : {packet.rssi:.1f} dBm")
        print(f"SNR          : {packet.snr:.2f} dB")
        print("\nDATABASE")
        print("----------------------------------------")
        print(f"Packet ID       : {packet_id}")
        print("✓ AQI result saved successfully")
        print("==================================================\n")
