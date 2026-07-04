from database.engine import SessionLocal

from configuration.standard_models import AQIStandard
from configuration.standard_manager import StandardManager


def initialize_standards():
    session = SessionLocal()
    manager = StandardManager(session)
    if manager.get_active_standard() is None:
        manager.save_standard(
            AQIStandard(
                name="CPCB",
                version="2024",
                country="India",
                active=True
            )
        )
    session.close()
    print("AQI Standards initialized.")


if __name__ == "__main__":
    initialize_standards()