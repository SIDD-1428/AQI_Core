from typing import Any

from .observation_window import ObservationWindow
from ..filters.filter_manager import FilterManager
from ..filters.filter_result import FilterResult


class ObservationProcessor:

    """Processes completed observation windows."""

    def __init__(self):

        self._filter_manager = FilterManager()


    def process(
        self,
        window: ObservationWindow,
        original_value: float | None = None
    ) -> FilterResult:

        if window is None:
            return FilterResult(
                success=False,
                reason="No observation window provided"
            )

        packets = window.get_packets()

        if not packets:
            return FilterResult(
                success=False,
                signal=window.signal,
                original_value=original_value,
                reason="Observation window contains no packets"
            )

        return self._filter_manager.filter_signal(
            signal=window.signal,
            packets=packets,
            original_value=original_value
        )