from configuration.breakpoint_repository import BreakpointRepository

class BreakpointManager:
    def __init__(self, session):
        self.repository=BreakpointRepository(session)
    
    def save_breakpoint(self,breakpoint):
        self.repository.save(breakpoint)
        
    def get_breakpoints(self,pollutant,standard_id):
        return self.repository.get_breakpoints(pollutant, standard_id)
    
    def breakpoint_exists(self,pollutant,standard_id,aqi_low,aqi_high):
        return(
            self.repository.exists(
                pollutant, standard_id, aqi_low, aqi_high
            )
        )