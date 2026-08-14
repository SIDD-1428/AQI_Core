from typing import Any
from .filter_result import FilterResult
from .median_filter import MedianFilter


class FilterManager:

    """Coordinates filtering of observed sensor signals."""
    def __init__(self):

        self._filters = {
            "median": MedianFilter()
        }


    def filter_signal(
        self,
        signal: str,
        packets: list[Any],
        original_value: float | None = None,
        method: str = "median"
    ) -> FilterResult:

        filter_engine = self._filters.get(method)

        if filter_engine is None:
            return FilterResult(
                success=False,
                signal=signal,
                original_value=original_value,
                method=method,
                reason=f"Unknown filtering method: {method}"
            )

        values = self._extract_values(
            signal,
            packets
        )

        result = filter_engine.apply(
            values,
            original_value=original_value
        )

        # FilterResult is frozen, so create a result
        # containing the signal name.
        return FilterResult(
            success=result.success,
            signal=signal,
            original_value=result.original_value,
            filtered_value=result.filtered_value,
            method=result.method,
            sample_count=result.sample_count,
            confidence=result.confidence,
            reason=result.reason
        )


    @staticmethod
    def _extract_values(
        signal: str,
        packets: list[Any]
    ) -> list[float]:

        values = []

        for packet in packets:
            value = getattr(
                packet,
                signal,
                None
            )

            if value is None:
                continue
            try:
                values.append(float(value))
            except (TypeError, ValueError):
                continue
        return values


    def available_methods(self) -> list[str]:
        return list(self._filters.keys())