from typing import Any

from ..context import PostProcessingContext
from aqi.engine import AQIEngine


class AQIValidator:
    """
    Validates the AQI calculated from the post-processed packet.

    This class does not implement AQI calculation itself.
    It delegates calculation to the existing AQIEngine so that
    first-processing and post-processing use the same AQI rules.
    """

    def __init__(self, aqi_engine: AQIEngine):

        self._aqi_engine = aqi_engine


    def validate(
        self,
        packet: Any,
        context: PostProcessingContext | None = None
    ) -> Any:

        if packet is None:

            raise ValueError(
                "Cannot validate AQI from an empty packet"
            )

        # Reuse the existing AQI calculation engine.
        result = self._aqi_engine.calculate(packet)

        if context is not None:

            context.metadata[
                "post_processed_aqi"
            ] = result.aqi

            context.metadata[
                "post_processed_category"
            ] = result.category

            context.metadata[
                "post_processed_dominant_pollutant"
            ] = result.dominant_pollutant

            context.metadata[
                "post_processed_subindices"
            ] = result.subindices

        return result