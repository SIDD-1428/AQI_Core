from fastapi import APIRouter
from api.services.aqi_service import AQIService

router=APIRouter()

@router.get("/aqi/latest")
def latest_aqi():
    service=AQIService()

    try:
        result=service.get_latest_aqi()

        if result is None:
            return {"message":"No AQI data available"}
        return{
            "aqi":result.aqi,
            "category":result.category,
            "dominant_pollutant":result.dominant_pollutant,
            "subindices":{
                "PM2_5": result.pm2_5_index,
                "PM10": result.pm10_index,
                "NO2":result.no2_index,
                "SO2":result.so2_index,
                "CO":result.co_index,
                "O3":result.o3_index,
                "NH3":result.nh3_index,
            }
        }
    
    finally:
        service.close()


@router.get("/aqi/history")
def aqi_history(limit: int=50):
    service=AQIService()

    try:
        results=service.get_history(limit)
        history=[]
        for result in results:
            history.append({
                "aqi":result.aqi,
                "category":result.category,
                "dominant_pollutant":result.dominant_pollutant,
                "created_at":result.created_at,
                "subindices":{
                    "PM2_5":result.pm2_5_index,
                    "PM10":result.pm10_index,
                    "NO2":result.no2_index,
                    "SO2":result.so2_index,
                    "CO":result.co_index,
                    "O3":result.o3_index,
                    "NH3":result.nh3_index,
                }
            })
        return history
    finally:
        service.close()
