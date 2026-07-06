from fastapi import APIRouter
from database.engine import SessionLocal
from database.models import Packet
from database.aqi_result_models import AQIResultModel
from api.schemas.system import SystemStatusResponse

router=APIRouter(tags=["System"])
@router.get("/system/status",response_model=SystemStatusResponse)
def system_status():
    session=SessionLocal()
    try:
        packet_count=session.query(Packet).count=session.query(AQIResultModel).count()
        aqi_count=session.query(AQIResultModel).count()
        return{
            "status":"online",
            "database":"connected",
            "version":"1.0.0",
            "packets":packet_count,
            "aqi_records":aqi_count
        }
    
    finally:
        session.close()