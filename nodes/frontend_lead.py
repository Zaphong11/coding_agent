from llm import make_llm
from state import AgentState, TaskPlan

llm = make_llm()

def frontend_lead_node(state: AgentState):
    tasks = state["plan"].frontend
    results = []
    for t in tasks:
        prompt = f"""Bạn là frontend coding worker chuyên React/TypeScript.
        Task: {t}
        Viết code hoàn chỉnh, ngắn gọn, kèm giải thích 1-2 câu."""
        res = llm.invoke(prompt)
        results.append(res.content)
        print(f"[frontend_lead] done task: {t}")
    return {"frontend_result": "\n\n".join(results)}