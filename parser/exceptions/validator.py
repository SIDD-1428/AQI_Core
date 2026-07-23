import math
from parser.entry_point.context import ProcessingContext
from parser.dataclass.exceptions import ValidationError


class PacketValidator:
    """
    Stage 3 of the processing pipeline.
    Validates all sensor values.
    """

    VALIDATION_RULES = {
        "temperature": {
            "normal": (-20.0, 50.0),
            "absolute": (-40.0, 85.0)
        },

        "humidity": {
            "normal": (20.0, 80.0),
            "absolute": (0.0, 100.0)
        },

        "pressure": {
            "normal": (900.0, 1100.0),
            "absolute": (300.0, 1200.0)
        },

        "pm1_0": {
            "normal": (0.0, 300.0),
            "absolute": (0.0, 1000.0)
        },

        "pm2_5": {
            "normal": (0.0, 300.0),
            "absolute": (0.0, 1000.0)
        },

        "pm10": {
            "normal": (0.0, 500.0),
            "absolute": (0.0, 1000.0)
        },

        "o3": {
            "normal": (0.0, 300.0),
            "absolute": (0.0, 1000.0)
        },

        "no2": {
            "normal": (0.0, 300.0),
            "absolute": (0.0, 1000.0)
        },

        "co": {
            "normal": (0.0, 100.0),
            "absolute": (0.0, 1000.0)
        },

        "nh3": {
            "normal": (0.0, 100.0),
            "absolute": (0.0, 1000.0)
        },

        "so2": {
            "normal": (0.0, 300.0),
            "absolute": (0.0, 1000.0)
        },

        "rssi": {
            "normal": (-110, 0),
            "absolute": (-150, 0)
        },

        "snr": {
            "normal": (-20, 20),
            "absolute": (-30, 30)
        }

    }

    def process(self, context: ProcessingContext) -> ProcessingContext:
        packet = context.packet

        if packet is None:
            raise ValidationError("Packet has not been parsed.")

        for field, limits in self.VALIDATION_RULES.items():
            value = getattr(packet, field)

        
            if value is None:
                raise ValidationError(f"{field} is missing.")
        
            if not isinstance(value, (int, float)):
                raise ValidationError(
                    f"{field} must be numeric."
                )

            if math.isnan(value):
                raise ValidationError(
                    f"{field} contains NaN."
                )

            if math.isinf(value):
                raise ValidationError(
                    f"{field} contains Infinity."
                )

            absolute_min, absolute_max = limits["absolute"]

            if value < absolute_min or value > absolute_max:
                raise ValidationError(
                    f"{field} value {value} outside absolute range."
                )

            normal_min, normal_max = limits["normal"]

            if value < normal_min or value > normal_max:

                context.warnings.append({
                    "field": field,
                    "value": value,
                    "severity": "warning",
                    "message": "Outside normal operating range."
                })

                context.quality_score = max(
                    0,
                    context.quality_score - 5
                )

        context.metadata["validator"] = "passed"

        return context