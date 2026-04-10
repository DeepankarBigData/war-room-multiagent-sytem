import logging

logger = logging.getLogger(__name__)

def calculate_risk_score(state):
    logger.info("[RISK_TOOL] Calculating risk score")
    try:
        risk = 0

        if state["metrics_summary"]["crash_change"] > 0.5:
            logger.debug("[RISK_TOOL] High crash rate - adding 0.4 to risk")
            risk += 0.4

        if state["metrics_summary"]["max_payment_failure"] > 4:
            logger.debug("[RISK_TOOL] High payment failure - adding 0.4 to risk")
            risk += 0.4

        if state["feedback_summary"]["negative"] > state["feedback_summary"]["positive"]:
            logger.debug("[RISK_TOOL] Negative feedback dominant - adding 0.2 to risk")
            risk += 0.2

        final_score = min(risk, 1.0)
        logger.info(f"[RISK_TOOL] Final risk score: {final_score}")
        return final_score
    except Exception as e:
        logger.error(f"[RISK_TOOL] Error calculating risk score: {str(e)}", exc_info=True)
        raise