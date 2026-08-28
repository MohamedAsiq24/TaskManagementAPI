from fastapi import FastAPI
from app.api.routes.auth import router as auth_router

app = FastAPI(title = "Task Management API",version="1.0.0",description="REST API with JWT Authentication")

app.include_router(auth_router)

@app.get("/")
def root():
    return {"message":"Task Management API is running"}

@app.get("/health")
def health_check():
    return {"status": "Healthy"}

         