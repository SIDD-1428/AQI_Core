from dataclasses import dataclass, field
from typing import Any
from datetime import datetime

@dataclass
class ObservationWindow:
    timestamp:datetime
    value:float
    packet:Any
    signal:str
    reason:str
    window_size: int = 10
    packets: list[Any]=field(default_factory=list)
    completed: bool=False

    def add_packet(self,packet:Any):
        if self.completed:
            return
        self.packets.append(packet)

        if len(self.packets)>= self.window_size:
            self.completed=True


    def is_complete(self)->bool:
        return self.completed

    def collected(self)->int:
        return len(self.packets)

    def remaining(self)->int:
        return max(0,self.window_size-len(self.packets))

    def clear(self):
        self.packets.clear()
        self.completed=False