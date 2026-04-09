def marketing_agent(state, llm):
    prompt = f"""
    Feedback: {state['feedback_summary']}

    What is user perception?
    """

    response = llm.invoke(prompt)
    # print(f"Marketing agent response: {response.content}")

    return {
        **state,
        "marketing_analysis": response.content
    }