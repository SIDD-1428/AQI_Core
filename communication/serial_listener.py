import serial

from config.config import SERIAL_PORT
from config.config import BAUD_RATE
from config.config import SERIAL_TIMEOUT

class SerialListener:
    print("Loaded:", __file__)
    def __init__(self):
        self.serial_port=serial.Serial(
            port=SERIAL_PORT,
            baudrate=BAUD_RATE,
            timeout=SERIAL_TIMEOUT
        )
    
    def read_line(self):
        try:
            if self.serial_port.in_waiting==0:
                return None
            
            line=self.serial_port.readline().decode("utf-8", errors="ignore").strip()
            if not line:
                return None
            
            if not line.startswith("{"):
                return None

            return line
        except serial.SerialException as e:
            print(f"Serial Error: {e}")
            return None

    
    """def read_line(self):
        print("Bytes waiting:",
        self.serial_port.in_waiting)

        if self.serial_port.in_waiting==0:
            return None
        
        line=self.serial_port.readline().decode(
            "utf-8",errors="ignore"
        ).strip()

        print("Received: ",repr(line))

        return line"""