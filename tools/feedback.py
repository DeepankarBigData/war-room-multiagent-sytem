import logging

logger = logging.getLogger(__name__)

def analyze_feedback(feedback):
    logger.info(f"[FEEDBACK_TOOL] Analyzing feedback - total entries: {len(feedback)}")
    try:
        negative_keywords = ["fail", "crash", "slow", "error"]

        negative = sum(any(k in f.lower() for k in negative_keywords) for f in feedback)
        positive = len(feedback) - negative

        logger.info(f"[FEEDBACK_TOOL] Feedback analysis: positive={positive}, negative={negative}")
        
        return {
            "positive": positive,
            "negative": negative
        }
    except Exception as e:
        logger.error(f"[FEEDBACK_TOOL] Error analyzing feedback: {str(e)}", exc_info=True)
        raise