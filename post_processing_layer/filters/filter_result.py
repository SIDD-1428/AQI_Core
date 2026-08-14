from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class FilterResult:
    """Result produced by a post-processing filter."""
    success: bool
    signal: str | None = None
    original_value: float | None = None
    filtered_value: float | None = None
    method: str = ""
    sample_count: int = 0
    confidence: float = 0.0
    reason: str = ""