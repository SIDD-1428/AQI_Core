from collections import deque
from typing import Any

class HistoryBuffer:
    def __init__(self,max_size:int=100):
        self._buffer=deque(maxlen=max_size)

    def add(self, packet:Any)-> None:
        self._buffer.append(packet)

    def get_all(self)->list[Any]:
        return list(self._buffer)

    def get_last(self,count: int =1)->list[Any]:
        if count<=0:
            return []
        return list(self._buffer)[-count:]

    def latest(self)->Any | None:
        if not self._buffer:
            return None
        return self._buffer[-1]

    def clear(self)-> None:
        self._buffer.clear()

    def size(self)->int:
        return len(self._buffer)

    def is_empty(self)->bool:
        return len(self._buffer)==0
