from typing import List

from fastapi import APIRouter, HTTPException

from aqi.rounding import round_aqi_index
from api.schemas.aqi import AQIResponse
from api.services.aqi_service import AQIService


router = APIRouter(tags=["AQI"])


def _serialize_aqi_result(result):
    """Normalize legacy fractional database values for the integer AQI API."""
    def normalize(value):
        return round_aqi_index(value) if value is not None else None

    return {
        "aqi": normalize(result.aqi),
        "category": result.category,
        "dominant_pollutant": result.dominant_pollutant,
        "created_at": result.created_at,
        "subindices": {
            "PM2_5": normalize(result.pm2_5_index),
            "PM10": normalize(result.pm10_index),
            "NO2": normalize(result.no2_index),
            "SO2": normalize(result.so2_index),
            "CO": normalize(result.co_index),
            "O3": normalize(result.o3_index),
            "NH3": normalize(result.nh3_index),
        },
    }


@router.get("/aqi/latest", response_model=AQIResponse)
def latest_aqi():
    service = AQIService()
    try:
        result = service.get_latest_aqi()
        if result is None:
            raise HTTPException(
                status_code=404,
                detail="No AQI data available"
            )
        return _serialize_aqi_result(result)
    finally:
        service.close()


@router.get("/aqi/history", response_model=List[AQIResponse])
def aqi_history(limit: int = 50):
    service = AQIService()
    try:
        results = service.get_history(limit)
        return [_serialize_aqi_result(result) for result in results]
    finally:
        service.close()
