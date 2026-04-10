import logging
from tools.anomaly import detect_anomaly

logger = logging.getLogger(__name__)

def data_agent(state):
    logger.info("[DATA_AGENT] Starting data agent")
    try:
        anomaly = detect_anomaly(state["metrics_summary"])
        logger.info(f"[DATA_AGENT] Anomaly detection result: {anomaly}")
        logger.info("[DATA_AGENT] Data agent completed successfully")

        return {
            **state,
            "data_analysis": anomaly
        }
    except Exception as e:
        logger.error(f"[DATA_AGENT] Error in data agent: {str(e)}", exc_info=True)
        raise