from aqi.models import AQIResult

class AQIEngine:
    def __init__(self, breakpoint_manager,standard_manager):
        self.breakpoint_manager=breakpoint_manager
        self.standard_manager=standard_manager

    def find_breakpoint(self,pollutant,concentration):
        standard=self.standard_manager.get_active_standard()

        print("Standard:", standard.id)
        print("Pollutant:", pollutant)
        print("Concentration:", concentration)

        breakpoints=self.breakpoint_manager.get_breakpoints(pollutant,standard.id)
        print("Number of BreakpointsL ",len(breakpoints))
        for bp in breakpoints:
            print(bp.conc_low, bp.conc_high)
            if bp.conc_low<= concentration <= bp.conc_high:
                print("Match Found")
                return bp
        print("No match")
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
        breakpoint=self.find_breakpoint("PM2_5",packet.pm2_5)
        
        if breakpoint is None:
            return None
        
        aqi=round(self.calculate_subindex(packet.pm2_5,breakpoint))
        return AQIResult(
            aqi=aqi,
            category=breakpoint.category,
            color=breakpoint.color,
            dominant_pollutant="PM2.5"
        )