from fastapi import APIRouter
from api.schemas.health import HealthResponse
router=APIRouter(tags=["Health"])

@router.get("/health",response_model=HealthResponse)
def health():
    return{
        "status":"ok",
        "service":"AQI Core",
        "version":"1.0.0"
    }