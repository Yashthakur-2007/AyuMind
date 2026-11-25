
from fastapi import FastAPI
from app.routers.upload import router as upload_router

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Medical Auditor API Running"}


app.include_router(upload_router)
