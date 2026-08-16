from database.models import Packet
from database.engine import SessionLocal

from configuration.breakpoint_manager import BreakpointManager
from configuration.standard_manager import StandardManager
from aqi.engine import AQIEngine

from post_processing_layer.post_processing_engine import PostProcessingEngine
from post_processing_layer.history.history_manager import HistoryManager


def create_test_packet(sequence: int, pm2_5: float) -> Packet:

    return Packet(
        version=1,
        node="TEST_NODE",
        sequence=sequence,

        temperature=25.0,
        humidity=60.0,
        pressure=1013.0,

        pm1_0=20.0,
        pm2_5=pm2_5,
        pm10=30.0,

        o3=10.0,
        no2=10.0,
        co=1.0,
        nh3=5.0,
        so2=5.0,

        rssi=-45.0,
        snr=10.0,

        checksum=0,
        valid=True,
        timestamp=sequence
    )


def main():

    session = SessionLocal()

    breakpoint_manager = BreakpointManager(session)
    standard_manager = StandardManager(session)

    aqi_engine = AQIEngine(
        breakpoint_manager,
        standard_manager
    )

    post_processing_engine = PostProcessingEngine(
        aqi_engine=aqi_engine
    )

    history_manager = HistoryManager()

    test_values = [
    52, 53, 200, 54, 52, 53, 51, 52, 54, 53,
    52, 53, 53, 53, 53, 53, 53 ]

    print("\n")
    print("=" * 70)
    print("POST-PROCESSING TEST")
    print("=" * 70)

    for sequence, pm2_5 in enumerate(test_values, start=1):

        packet = create_test_packet(
            sequence=sequence,
            pm2_5=pm2_5
        )

        initial_aqi = aqi_engine.calculate(packet)

        context = post_processing_engine.process(
            packet=packet,
            history=history_manager
        )

        print("\n" + "-" * 70)
        print(
            f"PACKET #{sequence} | "
            f"PM2.5 = {pm2_5}"
        )
        print("-" * 70)

        print(
            f"Initial AQI          : "
            f"{initial_aqi.aqi}"
        )

        print(
            f"Stage                : "
            f"{context.current_stage}"
        )

        print(
            f"Anomaly detected     : "
            f"{context.anomaly_detected}"
        )

        print(
            f"Observation started  : "
            f"{context.observation_started}"
        )

        print(
            f"Final result ready   : "
            f"{context.final_result_available}"
        )

        if context.filtered_packet is not None:

            print(
                f"Filtered PM2.5      : "
                f"{context.filtered_packet.pm2_5}"
            )

        if context.report is not None:

            print(
                f"Final AQI            : "
                f"{context.report.aqi}"
            )

            print(
                f"Final category       : "
                f"{context.report.category}"
            )

        if context.warnings:

            print("Warnings:")

            for warning in context.warnings:
                print(f"  - {warning}")

        # IMPORTANT:
        # Add to history only AFTER processing.
        history_manager.add_packet(packet)

    print("\n")
    print("=" * 70)
    print("TEST COMPLETE")
    print("=" * 70)

    session.close()


if __name__ == "__main__":
    main()