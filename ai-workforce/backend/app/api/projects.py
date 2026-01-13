import uuid
from fastapi import APIRouter
from app.orchestration.state import ProjectState
from app.agents.project_manager import run as pm_run

router = APIRouter(prefix="/projects", tags=["projects"])

PROJECT_STORE = {}  # temporary (Supabase later)

@router.post("")
def create_project(payload: dict):
    user_prompt = payload.get("prompt")

    if not user_prompt:
        return {"error": "Prompt is required"}

    project_id = str(uuid.uuid4())

    state: ProjectState = {
        "project_id": project_id,
        "user_prompt": user_prompt,
        "assumptions": [],
        "modules": [],
        "phases": [],
        "tasks": {},
        "files": {},
        "logs": [],
        "status": "created"
    }

    # Run PM AI (planning only)
    state = pm_run(state)

    PROJECT_STORE[project_id] = state

    return {
        "project_id": project_id,
        "status": state["status"]
    }
