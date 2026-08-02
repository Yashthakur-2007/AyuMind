from fastapi import FastAPI
from app.routers import health

app = FastAPI(
    title="Medical Auditor API",
    description="Backend API for AI Clinical Case Auditor",
    version="1.0.0"
)

app.include_router(health.router)

@app.get("/")
def root():
    return {
        "message": "Welcome to Medical Auditor API"
    }