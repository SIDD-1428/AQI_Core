from aqi.models import AQIResult

class AQIEngine:
    def __init__(self, breakpoint_manager,standard_manager):
        self.breakpoint_manager=breakpoint_manager
        self.standard_manager=standard_manager

    def find_breakpoint(self,pollutant,concentration):
        standard=self.standard_manager.get_active_standard()

        #print("Standard:", standard.id)
        #print("Pollutant:", pollutant)
        #print("Concentration:", concentration)

        breakpoints=self.breakpoint_manager.get_breakpoints(pollutant,standard.id)
        #print("Number of Breakpoints: ",len(breakpoints))
        for bp in breakpoints:
            #print(bp.conc_low, bp.conc_high)
            if bp.conc_low<= concentration <= bp.conc_high:
                #print("Match Found")
                return bp
        #print("No match")
        return None
        
        
    def calculate_subindex(self,concentration,breakpoint):
        i_hi=breakpoint.aqi_high
        i_lo=breakpoint.aqi_low
        bp_hi=breakpoint.conc_high
        bp_lo=breakpoint.conc_low

        return(
                ((i_hi-i_lo)/(bp_hi-bp_lo))*(concentration-bp_lo)+i_lo
            )
    
    def calculate(self,packet):
        pollutants={
            "PM2_5":packet.pm2_5,
            "PM10":packet.pm10,
            "NO2":packet.no2,
            "SO2":packet.so2,
            "CO":packet.co,
            "O3":packet.o3,
            "NH3":packet.nh3
        }
        subindices={}
        for pollutant, concentration in pollutants.items():
            breakpoint=self.find_breakpoint(pollutant,concentration)
            if breakpoint is None:
                continue

            subindex=round(
                self.calculate_subindex(concentration,breakpoint)
            )

            subindices[pollutant]={
                "aqi":subindex,
                "breakpoint":breakpoint
            }
        dominant_pollutant=max(subindices, key=lambda pollutant:subindices[pollutant]["aqi"])
        dominant=subindices[dominant_pollutant]

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