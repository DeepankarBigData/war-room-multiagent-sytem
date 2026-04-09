from tools.anomaly import detect_anomaly


def data_agent(state):
    anomaly = detect_anomaly(state["metrics_summary"])

    return {
        **state,
        "data_analysis": anomaly
    }