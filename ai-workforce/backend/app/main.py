from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.projects import router as projects_router

app = FastAPI(title="AI Workforce Backend")

app.include_router(health_router)
app.include_router(projects_router)

@app.get("/")
def root():
    return {"status": "AI Workforce backend running"}
