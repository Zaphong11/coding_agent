from llm import make_llm
from state import AgentState, TaskPlan

llm = make_llm()

# ---- ORCHESTRATOR NODE ----
def orchestrator_node(state: AgentState):
    prompt = f"""Phân rã yêu cầu sau thành JSON với 3 key: backend, frontend, tester.
    Mỗi key là list các task cụ thể, ngắn gọn.
    CHỈ trả về JSON thuần, không markdown fence, không giải thích thêm.

    Yêu cầu: {state['request']}"""
    res = llm.invoke(prompt)
    plan = TaskPlan.model_validate_json(res.content)
    print(f"[orchestrator] plan: {plan}")
    return {"plan": plan}
