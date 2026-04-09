from tools.metrics import analyze_metrics
from tools.feedback import analyze_feedback


def preprocessing_node(state):
    print("Running preprocessing...")

    launch_day = state["release_notes"]["launch_day"]

    metrics_summary = analyze_metrics(state["metrics"], launch_day)
    feedback_summary = analyze_feedback(state["feedback"])

    return {
        **state,
        "metrics_summary": metrics_summary,
        "feedback_summary": feedback_summary
    }