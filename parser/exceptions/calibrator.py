from parser.entry_point.context import ProcessingContext
from parser.dataclass.exceptions import CalibrationError

class CalibrationEngine:
    """Stage4 of processing- calibrates the validated packets"""
    def process(self,context: ProcessingContext)->ProcessingContext:
        packet=context.packet
        if packet is None:
            raise CalibrationError("Packet has not been parsed")
        
        context.metadata["calibration"]={
            "profile":"default",
            "status":"[pass-through]"
        }

        return context