#generic importer
import json
from pathlib import Path

from database.engine import SessionLocal

from configuration.breakpoint_models import AQIBreakpoint
from configuration.breakpoint_repository import BreakpointRepository
from configuration.standard_manager import StandardManager

DATA_FILE=(
    Path(__file__).parent/"data"/"cpcb"/"naqi_2024.json"
)
    
def initialize_breakpoints():
    session=SessionLocal()
    repository = BreakpointRepository(session)
    standard_manager=StandardManager(session)
    standard=standard_manager.get_active_standard()
    if standard is None:
        print("No active AQI standard found")
        session.close()
        return
    with open(DATA_FILE, "r", encoding ="utf-8") as file:
        data=json.load(file)
        for pollutant, breakpoints in data["pollutants"].items():
            for item in breakpoints:
                breakpoint = AQIBreakpoint(
                    pollutant=pollutant,
                    standard_id=standard.id,
                    aqi_low=item["aqi_low"],
                    aqi_high=item["aqi_high"],
                    conc_low=item["conc_low"],
                    conc_high=item["conc_high"],
                    category=item["category"],
                    color=item["color"],
                    health_message=item["health_message"]
                )

                repository.save(breakpoint)
        session.close()
        print("AQI Breakpoints imported successfully.")


if __name__=="__main__":
    initialize_breakpoints()