def decision_node(state, llm):
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

    response = llm.invoke(prompt)

    return {
        **state,
        "final_decision": response.content
    }