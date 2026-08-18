from langgraph.graph import StateGraph, END
from state import AgentState
from nodes import orchestrator, backend_lead, frontend_lead, tester_lead

# ---- BUILD GRAPH ----
graph = StateGraph(AgentState)
graph.add_node("orchestrator", orchestrator.orchestrator_node)
graph.add_node("backend_lead", backend_lead.backend_lead_node)
graph.add_node("frontend_lead", frontend_lead.frontend_lead_node)
graph.add_node("tester", tester_lead.tester_node)

graph.set_entry_point("orchestrator")
graph.add_edge("orchestrator", "backend_lead")
graph.add_edge("backend_lead", "frontend_lead")
graph.add_edge("frontend_lead", "tester")
graph.add_edge("tester", END)

app = graph.compile()
