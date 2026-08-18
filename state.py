from pydantic import BaseModel
from typing import List, TypedDict

class TaskPlan(BaseModel):
    backend: List[str]
    frontend: List[str]
    tester: List[str]

class AgentState(TypedDict):
    request: str
    plan: TaskPlan
    backend_result: str
    frontend_result: str
    test_result: str
