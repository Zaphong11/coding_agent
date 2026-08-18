from llm import make_llm
from state import AgentState, TaskPlan

llm = make_llm()

def backend_lead_node(state: AgentState):
    tasks = state["plan"].backend
    results = []
    for t in tasks:
        prompt = f"""Bạn là backend coding worker chuyên Python/FastAPI.
        Task: {t}
        Viết code hoàn chỉnh, ngắn gọn, kèm giải thích 1-2 câu."""
        res = llm.invoke(prompt)
        results.append(res.content)
        print(f"[backend_lead] done task: {t}")
    return {"backend_result": "\n\n".join(results)}