from fastapi import FastAPI
from api.routes.aqi import router as aqi_router
from api.routes.health import router as health_router
from api.routes.packet import router as packet_router
from api.routes.node import router as node_router
from api.routes.system import router as system_router

app=FastAPI(
    title="AQI Core API",
    version="1.0.0",
    description="Backend API for AQI Core"
)

#Register routes
app.include_router(health_router)
app.include_router(aqi_router)
app.include_router(packet_router)
app.include_router(node_router)
app.include_router(system_router)