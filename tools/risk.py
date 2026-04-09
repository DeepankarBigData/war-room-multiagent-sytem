def calculate_risk_score(state):
    risk = 0

    if state["metrics_summary"]["crash_change"] > 0.5:
        risk += 0.4

    if state["metrics_summary"]["max_payment_failure"] > 4:
        risk += 0.4

    if state["feedback_summary"]["negative"] > state["feedback_summary"]["positive"]:
        risk += 0.2

    return min(risk, 1.0)