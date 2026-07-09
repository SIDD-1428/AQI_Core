from fastapi import FastAPI
from api.routes.aqi import router as aqi_router
from api.routes.health import router as health_router
from api.routes.packet import router as packet_router
from api.routes.node import router as node_router
from api.routes.system import router as system_router
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI(
    title="AQI Core API",
    version="1.0.0",
    description="Backend API for AQI Core"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Register routes
app.include_router(health_router)
app.include_router(aqi_router)
app.include_router(packet_router)
app.include_router(node_router)
app.include_router(system_router)