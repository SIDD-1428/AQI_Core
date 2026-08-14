from typing import Any

class ObservationBuffer:
    """Stores packets collected during an observation window."""

    def __init__(self, max_size: int = 10):
        self.max_size = max_size
        self._packets: list[Any] = []


    def add(self, packet: Any) -> None:
        if self.is_full():
            return

        self._packets.append(packet)


    def values(self) -> list[Any]:
        return self._packets.copy()


    def size(self) -> int:
        return len(self._packets)


    def is_full(self) -> bool:
        return len(self._packets) >= self.max_size


    def remaining(self) -> int:
        return max(
            0,
            self.max_size - len(self._packets)
        )


    def clear(self) -> None:
        self._packets.clear()