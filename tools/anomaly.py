import logging

logger = logging.getLogger(__name__)

def detect_anomaly(metrics_summary):
    logger.info("[ANOMALY_TOOL] Detecting anomalies")
    try:
        crash_change = metrics_summary["crash_change"]
        logger.debug(f"[ANOMALY_TOOL] Crash rate change: {crash_change}")
        
        if crash_change > 0.5:
            logger.warning(f"[ANOMALY_TOOL] ANOMALY DETECTED - Crash rate increased significantly by {crash_change}")
            return "Crash rate increased significantly"
        
        logger.info("[ANOMALY_TOOL] No major anomalies detected")
        return "No major anomaly"
    except Exception as e:
        logger.error(f"[ANOMALY_TOOL] Error detecting anomaly: {str(e)}", exc_info=True)
        raise