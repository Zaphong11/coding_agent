from llm import make_llm
from state import AgentState, TaskPlan

llm = make_llm()

def tester_node(state: AgentState):
    tasks = state["plan"].tester
    results = []
    for t in tasks:
        prompt = f"""Bạn là QA/testing worker chuyên kiểm thử ứng dụng web Python/FastAPI.
        Task: {t}
        Viết test hoàn chỉnh, ngắn gọn, kèm giải thích 1-2 câu."""
        res = llm.invoke(prompt)
        results.append(res.content)
        print(f"[tester] done task: {t}")
    return {"test_result": "\n\n".join(results)}