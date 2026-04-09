from typing import TypedDict, List, Dict


class AgentState(TypedDict):
    metrics: List[Dict]
    feedback: List[str]
    release_notes: Dict

    metrics_summary: Dict
    feedback_summary: Dict

    data_analysis: str
    pm_analysis: str
    marketing_analysis: str
    risk_analysis: str

    final_decision: Dict