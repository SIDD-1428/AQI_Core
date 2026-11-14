from database.engine import SessionLocal

from configuration.breakpoint_manager import BreakpointManager
from configuration.standard_manager import StandardManager

from aqi.engine import AQIEngine


class FakePacket:
    pm2_5 = 74
    pm10 = 120
    no2 = 30
    so2 = 18
    co = 1.4
    o3 = 65
    nh3 = 70


def main():
    session = SessionLocal()
    try:
        breakpoint_manager = BreakpointManager(session)
        standard_manager = StandardManager(session)
        standard = standard_manager.get_active_standard()

        if standard is None:
            raise RuntimeError("No active AQI standard is configured")

        engine = AQIEngine(breakpoint_manager, standard_manager)
        result = engine.calculate(FakePacket())

        if result is None:
            print("No AQI result: no pollutant matched a configured breakpoint.")
            return

        print()
        print("=" * 40)
        print("FINAL AQI RESULT")
        print("=" * 40)
        print(f"AQI                 : {result.aqi}")
        print(f"Category            : {result.category}")
        print(f"Color               : {result.color}")
        print(f"Dominant Pollutant  : {result.dominant_pollutant}")
        print("\nSub-indices")
        print("-" * 40)

        for pollutant, value in result.subindices.items():
            print(f"{pollutant:<8} : {value}")
    finally:
        session.close()


if __name__ == "__main__":
    main()
