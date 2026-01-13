from typing import TypedDict, List, Dict

class ProjectState(TypedDict):
    project_id: str
    user_prompt: str

    # PM AI outputs
    assumptions: List[str]
    modules: List[str]
    phases: List[str]
    tasks: Dict[str, List[str]]

    # Execution
    files: Dict[str, str]
    logs: List[str]
    status: str
