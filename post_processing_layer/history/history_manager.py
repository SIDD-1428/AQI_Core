from typing import Any
from .history_buffer import HistoryBuffer
from .packet_cache import PacketCache

class HistoryManager:
    def __init__(self, buffer_size: int=100):
        self._history=HistoryBuffer(max_size=buffer_size)
        self._cache=PacketCache()

    def add_packet(self, packet:Any)->None:
        self._history.add(packet)
        self._cache.update(packet)

    def latest_packet(self)-> Any| None:
        return self._cache.latest_packet
    
    def previous_packet(self)->Any|None:
        return self._cache.previous_packet
    
    def get_last_packets(self, count:int=1)->list[Any]:
        return self._history.get_last(count)

    def get_all_packets(self)->list[Any]:
        return self._history.get_all()
    
    def get_signal_history(self, signal:str, count: int=10)->list[Any]:
        packets=self._history.get_last(count)
        values=[]
        for packet in packets:
            if hasattr(packet,signal):
                values.append(getattr(packet,signal))
        return values
        
    def clear(self)->None:
        self._history.clear()
        self._cache.clear()

    def size(self)->int:
        return self._history.size()

    def is_empty(self)->bool:
        return self._history.is_empty()

   