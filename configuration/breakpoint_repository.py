from configuration.breakpoint_models import AQIBreakpoint

class BreakpointRepository:
    def __init__ (self, session):
        self.session=session
    
    def save(self, breakpoint):
        self.session.add(breakpoint)
        self.session.commit()
    
    def get_breakpoints(self, pollutant, standard_id):
        return(
            self.session.query(AQIBreakpoint).filter_by(pollutant=pollutant, standard_id=standard_id).order_by(AQIBreakpoint.conc_low).all()
        )