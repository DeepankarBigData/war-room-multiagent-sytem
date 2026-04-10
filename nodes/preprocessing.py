import logging
from tools.metrics import analyze_metrics
from tools.feedback import analyze_feedback

logger = logging.getLogger(__name__)

def preprocessing_node(state):
    logger.info("[PREPROCESSING] Starting preprocessing node")
    try:
        launch_day = state["release_notes"]["launch_day"]
        logger.debug(f"[PREPROCESSING] Launch day: {launch_day}")

        metrics_summary = analyze_metrics(state["metrics"], launch_day)
        logger.info(f"[PREPROCESSING] Metrics analyzed - conversion_change: {metrics_summary.get('conversion_change')}, crash_change: {metrics_summary.get('crash_change')}")
        
        feedback_summary = analyze_feedback(state["feedback"])
        logger.info(f"[PREPROCESSING] Feedback analyzed - positive: {feedback_summary.get('positive')}, negative: {feedback_summary.get('negative')}")

        logger.info("[PREPROCESSING] Preprocessing node completed successfully")
        return {
            **state,
            "metrics_summary": metrics_summary,
            "feedback_summary": feedback_summary
        }
    except Exception as e:
        logger.error(f"[PREPROCESSING] Error in preprocessing node: {str(e)}", exc_info=True)
        raise