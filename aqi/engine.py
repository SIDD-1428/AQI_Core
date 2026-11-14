import math

from aqi.models import AQIResult
from aqi.rounding import round_aqi_index


class AQIEngine:
    def __init__(self, breakpoint_manager, standard_manager):
        self.breakpoint_manager = breakpoint_manager
        self.standard_manager = standard_manager

    def find_breakpoint(self, pollutant, concentration):
        standard = self.standard_manager.get_active_standard()
        if standard is None:
            raise RuntimeError("No active AQI standard is configured")

        breakpoints = self.breakpoint_manager.get_breakpoints(
            pollutant,
            standard.id
        )

        for breakpoint in breakpoints:
            if breakpoint.conc_low <= concentration <= breakpoint.conc_high:
                return breakpoint

        return None

    def calculate_subindex(self, concentration, breakpoint):
        i_hi = breakpoint.aqi_high
        i_lo = breakpoint.aqi_low
        bp_hi = breakpoint.conc_high
        bp_lo = breakpoint.conc_low

        if bp_hi == bp_lo:
            raise ValueError(
                "Invalid AQI breakpoint: concentration range has zero width"
            )

        return (
            ((i_hi - i_lo) / (bp_hi - bp_lo))
            * (concentration - bp_lo)
            + i_lo
        )

    def calculate(self, packet):
        pollutants = {
            "PM2_5": packet.pm2_5,
            "PM10": packet.pm10,
            "NO2": packet.no2,
            "SO2": packet.so2,
            "CO": packet.co,
            "O3": packet.o3,
            "NH3": packet.nh3,
        }

        subindices = {}

        for pollutant, raw_concentration in pollutants.items():
            if raw_concentration is None:
                continue

            try:
                concentration = float(raw_concentration)
            except (TypeError, ValueError):
                continue

            if not math.isfinite(concentration):
                continue

            breakpoint = self.find_breakpoint(pollutant, concentration)
            if breakpoint is None:
                continue

            raw_subindex = self.calculate_subindex(
                concentration,
                breakpoint
            )
            subindex = round_aqi_index(raw_subindex)

            subindices[pollutant] = {
                "aqi": subindex,
                "breakpoint": breakpoint,
            }

        # A packet may not have any pollutant with a configured breakpoint.
        # Return no result instead of raising max() on an empty dictionary.
        if not subindices:
            return None

        dominant_pollutant = max(
            subindices,
            key=lambda name: subindices[name]["aqi"]
        )
        dominant = subindices[dominant_pollutant]

        return AQIResult(
            aqi=dominant["aqi"],
            category=dominant["breakpoint"].category,
            color=dominant["breakpoint"].color,
            dominant_pollutant=dominant_pollutant,
            subindices={
                pollutant: data["aqi"]
                for pollutant, data in subindices.items()
            }
        )
