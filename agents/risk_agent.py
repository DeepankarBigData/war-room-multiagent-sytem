import logging
from tools.risk import calculate_risk_score

logger = logging.getLogger(__name__)

def risk_agent(state):
    logger.info("[RISK_AGENT] Starting risk agent")
    try:
        score = calculate_risk_score(state)
        logger.info(f"[RISK_AGENT] Risk score calculated: {score}")
        logger.info("[RISK_AGENT] Risk agent completed")
        return {
            **state,
            "risk_analysis": f"Risk score: {score}"
        }
    except Exception as e:
        logger.error(f"[RISK_AGENT] Error in risk agent: {str(e)}", exc_info=True)
        raise