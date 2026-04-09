from langgraph.graph import StateGraph, END

from nodes.preprocessing import preprocessing_node
from agents.data_agent import data_agent
from agents.pm_agent import pm_agent
from agents.marketing_agent import marketing_agent
from agents.risk_agent import risk_agent
from nodes.decision import decision_node


def build_graph(llm):
    builder = StateGraph(dict)

    builder.add_node("preprocessing", preprocessing_node)
    builder.add_node("data", data_agent)
    builder.add_node("pm", lambda state: pm_agent(state, llm))
    builder.add_node("marketing", lambda state: marketing_agent(state, llm))
    builder.add_node("risk", risk_agent)
    builder.add_node("decision", lambda state: decision_node(state, llm))

    builder.set_entry_point("preprocessing")

    builder.add_edge("preprocessing", "data")
    builder.add_edge("data", "pm")
    builder.add_edge("pm", "marketing")
    builder.add_edge("marketing", "risk")
    builder.add_edge("risk", "decision")
    builder.add_edge("decision", END)

    return builder.compile()