import logging

logger = logging.getLogger(__name__)

def marketing_agent(state, llm):
    logger.info("[MARKETING_AGENT] Starting marketing agent")
    try:
        prompt = f"""
    Feedback: {state['feedback_summary']}

    What is user perception?
    """
        logger.debug("[MARKETING_AGENT] Invoking LLM for user perception analysis")
        response = llm.invoke(prompt)
        logger.info(f"[MARKETING_AGENT] User perception analysis generated")
        logger.info("[MARKETING_AGENT] Marketing agent completed")

        return {
            **state,
            "marketing_analysis": response.content
        }
    except Exception as e:
        logger.error(f"[MARKETING_AGENT] Error in marketing agent: {str(e)}", exc_info=True)
        raise