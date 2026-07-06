from fastapi import FastAPI
from api.routes.aqi import router as aqi_router
from api.routes.health import router as health_router

app=FastAPI(
    title="AQI Core API",
    version="1.0.0",
    description="Backend API for AQI Core"
)

#Register routes
app.include_router(health_router)
app.include_router(aqi_router)