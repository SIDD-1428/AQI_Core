from typing import Any

from ..context import PostProcessingContext
from aqi.engine import AQIEngine


class AQIValidator:
    """Validates a post-processed packet using the shared AQI engine."""

    def __init__(self, aqi_engine: AQIEngine):
        self._aqi_engine = aqi_engine

    def validate(
        self,
        packet: Any,
        context: PostProcessingContext | None = None
    ) -> Any:
        if packet is None:
            raise ValueError("Cannot validate AQI from an empty packet")

        result = self._aqi_engine.calculate(packet)

        # No matching breakpoint is a valid "no AQI available" outcome.
        if result is None:
            if context is not None:
                context.warnings.append(
                    "AQI could not be calculated: no pollutant matched "
                    "a configured breakpoint"
                )
            return None

        if context is not None:
            context.metadata["post_processed_aqi"] = result.aqi
            context.metadata["post_processed_category"] = result.category
            context.metadata["post_processed_dominant_pollutant"] = (
                result.dominant_pollutant
            )
            context.metadata["post_processed_subindices"] = result.subindices

        return result
