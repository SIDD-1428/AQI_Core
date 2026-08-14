from statistics import median
from typing import Any

from .base_filter import BaseFilter
from .filter_result import FilterResult


class MedianFilter(BaseFilter):

    """Filters a signal using the statistical median."""

    def apply(
        self,
        values: list[Any],
        original_value: float | None = None
    ) -> FilterResult:

        if not values:
            return FilterResult(
                success=False,
             original_value=original_value,
                method="median",
                reason="No values available for filtering"
            )

        try:
            numeric_values = [
                float(value)
                for value in values
            ]

        except (TypeError, ValueError):

            return FilterResult(
                success=False,
                original_value=original_value,
                method="median",
                reason="Values contain non-numeric data"
            )

        filtered_value = median(numeric_values)

        return FilterResult(
            success=True,
            original_value=original_value,
            filtered_value=filtered_value,
            method="median",
            sample_count=len(numeric_values),
            confidence=1.0,
            reason=(
                f"Median calculated from "
                f"{len(numeric_values)} observations"
            )
        )