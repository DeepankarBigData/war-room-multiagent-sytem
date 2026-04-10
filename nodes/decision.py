import logging

logger = logging.getLogger(__name__)

def decision_node(state, llm):
    logger.info("[DECISION_NODE] Starting decision node")
    try:
        prompt = f"""
    You are a senior decision maker in a product war room.

    Inputs:
    Metrics Summary: {state['metrics_summary']}
    Feedback Summary: {state['feedback_summary']}
    Data Analysis: {state['data_analysis']}
    PM Analysis: {state['pm_analysis']}
    Marketing Analysis: {state['marketing_analysis']}
    Risk Analysis: {state['risk_analysis']}

    STRICT RULES:
    - If payment failures or crashes increased significantly → DO NOT proceed
    - If system stability is compromised → choose Pause or Rollback
    - Revenue improvement alone is NOT enough to proceed

    Produce a final JSON output with this exact structure:
    {{
      "decision": "Proceed | Pause | Rollback",
      "rationale": "key drivers with metric references and feedback summary",
      "risk_register": [
        {{
          "risk": "top risk description",
          "impact": "high/medium/low",
          "mitigation": "specific mitigation steps"
        }}
      ],
      "action_plan_24_48h": [
        {{
          "action": "specific action item",
          "owner": "responsible team/person",
          "timeline": "24h or 48h"
        }}
      ],
      "communication_plan": {{
        "internal": "messaging guidance for internal teams",
        "external": "messaging guidance for customers/users"
      }},
      "confidence_score": {{
        "score": "high/medium/low",
        "factors": "what would increase confidence to proceed"
      }}
    }}
    """
        logger.debug("[DECISION_NODE] Invoking LLM for final decision")
        response = llm.invoke(prompt)
        logger.debug(f"[DECISION_NODE] Raw response: {response}")
        logger.debug(f"[DECISION_NODE] Response type: {type(response)}")
        logger.debug(f"[DECISION_NODE] Response content: {response.content if hasattr(response, 'content') else 'NO CONTENT ATTR'}")
        
        final_decision = response.content if hasattr(response, 'content') else str(response)
        logger.info(f"[DECISION_NODE] Final decision generated (length: {len(final_decision)})")
        logger.info("[DECISION_NODE] Decision node completed")

        return {
            **state,
            "final_decision": final_decision
        }
    except Exception as e:
        logger.error(f"[DECISION_NODE] Error in decision node: {str(e)}", exc_info=True)
        raise