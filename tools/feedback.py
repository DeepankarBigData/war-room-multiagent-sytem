def analyze_feedback(feedback):
    negative_keywords = ["fail", "crash", "slow", "error"]

    negative = sum(any(k in f.lower() for k in negative_keywords) for f in feedback)
    positive = len(feedback) - negative

    return {
        "positive": positive,
        "negative": negative
    }