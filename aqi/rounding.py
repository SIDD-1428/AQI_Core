from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


def round_aqi_index(value: int | float | Decimal) -> int:
    """Round a non-negative AQI index to the nearest whole number.

    ROUND_HALF_UP avoids Python's ties-to-even behavior for .5 values.
    """
    try:
        number = Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError) as exc:
        raise ValueError(f"Invalid AQI index value: {value!r}") from exc

    if not number.is_finite():
        raise ValueError(f"AQI index must be finite, got {value!r}")

    return int(number.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
