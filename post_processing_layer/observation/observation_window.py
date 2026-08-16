from dataclasses import dataclass, field
from typing import Any
from .buffer import ObservationBuffer


@dataclass
class ObservationWindow:

    signal: str
    reason: str
    window_size: int = 10
    trigger_packet:Any | None= None
    buffer: ObservationBuffer = field(init=False)
    completed: bool = False


    def __post_init__(self) -> None:
        self.buffer = ObservationBuffer(
            max_size=self.window_size
        )


    def add_packet(self, packet: Any) -> None:
        if self.completed:
            return

        self.buffer.add(packet)

        if self.buffer.is_full():
            self.completed = True


    def is_complete(self) -> bool:
        return self.completed


    def collected(self) -> int:
        return self.buffer.size()


    def remaining(self) -> int:
        return self.buffer.remaining()


    def get_packets(self) -> list[Any]:
        return self.buffer.values()


    def clear(self) -> None:
        self.buffer.clear()
        self.completed = False
        self.trigger_packet=None