import logging

logger = logging.getLogger(__name__)

def pm_agent(state, llm):
    logger.info("[PM_AGENT] Starting PM agent")
    try:
        prompt = f"""
    <role>You are an expert product manager analyst in a war room.</role>
    <goal>Summarize the business impact of the feature launch using metrics and feedback.</goal>

    Inputs:
    Metrics Summary: {state['metrics_summary']}
    Feedback Summary: {state['feedback_summary']}

    <output_format>
    Return a STRICT JSON object exactly in this shape:
    {{
      "business_impact": "string",
      "top_drivers": ["string"],
      "critical_risks": ["string"],
      "recommended_next_step": "Proceed | Pause | Roll Back",
      "confidence": "high | medium | low",
      "confidence_drivers": "string"
    }}
    </output_format>

    <global_rules>
      1. Output only valid JSON, with no markdown and no extra text.
      2. Use metric values from metrics_summary whenever you refer to business impact.
      3. Use feedback themes from feedback_summary whenever possible.
      4. If crashes or payment failures increased significantly, recommend Pause or Roll Back.
      5. Keep each field concise and focused on business outcomes.
    </global_rules>
    """
        logger.debug("[PM_AGENT] Invoking LLM for business impact analysis")
        response = llm.invoke(prompt)
        logger.info(f"[PM_AGENT] PM analysis generated successfully")
        logger.info("[PM_AGENT] PM agent completed")
        
        return {
            **state,
            "pm_analysis": response.content
        }
    except Exception as e:
        logger.error(f"[PM_AGENT] Error in PM agent: {str(e)}", exc_info=True)
        raise