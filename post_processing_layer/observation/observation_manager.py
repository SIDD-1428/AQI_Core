from typing import Any
from .observation_window import ObservationWindow

class ObservationManager:
    """Manages active and completed observation windows. It starts observations, feeds incoming packets, and trscks completed observations"""
    def __init__(self):
        self._active_windows:dict[str,ObservationWindow]={}
        self._completed_windows: list[ObservationWindow]=[]

    def start_observation(
            self,
            signal:str,
            reason:str,
            window_size:int=7
    )->None:

        if signal in self._active_windows:
            return 

        self._active_windows[signal]=ObservationWindow(
            signal=signal,
            reason=reason,
            window_size=window_size
        )


    def process_packet(self,packet: Any)->None:
        completed: list[str]=[]

        for signal,window in self._active_windows.items():
            window.add_packet(packet)
            if window.is_complete():
                completed.append(signal)

        for signal in completed:
            window=self._active_windows.pop(signal)
            self._completed_windows.append(window)


    def get_completed_windows(self)->list[ObservationWindow]:
        return self._completed_windows.copy()


    def clear_completed(self)->None:
        self._completed_windows.clear()

    def has_completed_windows(self)->bool:
        return len(self._completed_windows)>0

    #queries
    def is_observing(self,signal:str)->bool:
        return signal in self._active_windows

    def get_window(self,signal:str)-> ObservationWindow | None:
        return self._active_windows.get(signal)

    def active_signals(self)->list[str]:
        return list(self._active_windows.keys())

    def active_count(self)->int:
        return len(self._active_windows)
    
    def clear(self)->None:
        self._active_windows.clear()
        self._completed_windows.clear()
