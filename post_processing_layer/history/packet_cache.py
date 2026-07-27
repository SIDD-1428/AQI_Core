from dataclasses import dataclass
from typing import Any

@dataclass
class PacketCache:
    lates_packet: Any | None=None
    previous_packet:Any | None=None
    latest_timestamp:Any | None=None

    def update(self,packet: Any):
        self.previous_packet=self.latest_packet
        self.latest_packet=packet
        self.latest_timestamp=getattr(packet,"timestamp",None)

    def clear(self):
        self.latest_packet=None
        self.previous_packet=None
        self.latest_timestamp=None
