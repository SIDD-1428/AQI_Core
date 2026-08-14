from abc import ABC, abstractmethod
from typing import Any

from .filter_result import FilterResult


class BaseFilter(ABC):

    """Base interface for all post-processing filters."""

    @abstractmethod
    def apply(
        self,
        values: list[Any],
        original_value: float | None = None
    ) -> FilterResult:
        """Apply the filtering strategy to the supplied values."""
        raise NotImplementedError