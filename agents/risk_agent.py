from tools.risk import calculate_risk_score


def risk_agent(state):
    score = calculate_risk_score(state)
    # print(f"Risk agent calculated score: {score}")
    return {
        **state,
        "risk_analysis": f"Risk score: {score}"
    }