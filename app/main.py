from fastapi import FastAPI

app = FastAPI(title = "Task Management API",version="1.0.0",description="REST API with JWT Authentication")

@app.get("/")
def root():
    return {"message":"Task Management API is running"}

@app.get("/health")
def health_check():
    return {"status": "Healthy"}

         