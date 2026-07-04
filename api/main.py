from fastapi import FastAPI

app=FastAPI(
    title="AQI Core API",
    version="1.0.0",
    description="Backend API for AQI Core"
)

@app.get("/")
def root():
    return{
        "message":"Welcome to AQI Core API"
    }

@app.get("/health")
def health():
    return{
    "status":"online",
    "service":"AQI Core API",
    "version":"1.0.0"
    }