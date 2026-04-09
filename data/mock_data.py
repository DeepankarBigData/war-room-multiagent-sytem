# FULL DATASET (Ready to Use)
# 🔢 A) Metrics (14 Days Time Series)
metrics_data = [
    {"day": "Day 1", "conversion": 12.0, "dau": 1000, "crash_rate": 0.5, "payment_failure": 2.0, "latency": 200, "tickets": 20},
    {"day": "Day 2", "conversion": 12.5, "dau": 1050, "crash_rate": 0.4, "payment_failure": 2.1, "latency": 210, "tickets": 18},
    {"day": "Day 3", "conversion": 13.0, "dau": 1100, "crash_rate": 0.5, "payment_failure": 2.2, "latency": 220, "tickets": 22},
    {"day": "Day 4", "conversion": 12.8, "dau": 1150, "crash_rate": 0.6, "payment_failure": 2.0, "latency": 210, "tickets": 19},
    {"day": "Day 5", "conversion": 13.2, "dau": 1200, "crash_rate": 0.5, "payment_failure": 2.1, "latency": 200, "tickets": 20},
    {"day": "Day 6", "conversion": 13.0, "dau": 1250, "crash_rate": 0.4, "payment_failure": 2.0, "latency": 205, "tickets": 21},
    {"day": "Day 7", "conversion": 13.1, "dau": 1300, "crash_rate": 0.5, "payment_failure": 2.1, "latency": 210, "tickets": 20},

    # 🚀 Feature launch happens here
    {"day": "Day 8", "conversion": 16.0, "dau": 1400, "crash_rate": 1.5, "payment_failure": 5.5, "latency": 350, "tickets": 45},
    {"day": "Day 9", "conversion": 15.8, "dau": 1450, "crash_rate": 1.4, "payment_failure": 5.2, "latency": 340, "tickets": 50},
    {"day": "Day 10", "conversion": 15.5, "dau": 1500, "crash_rate": 1.3, "payment_failure": 5.0, "latency": 330, "tickets": 48},
    {"day": "Day 11", "conversion": 15.2, "dau": 1520, "crash_rate": 1.2, "payment_failure": 4.8, "latency": 320, "tickets": 46},
    {"day": "Day 12", "conversion": 15.0, "dau": 1550, "crash_rate": 1.1, "payment_failure": 4.6, "latency": 310, "tickets": 44},
    {"day": "Day 13", "conversion": 14.8, "dau": 1580, "crash_rate": 1.0, "payment_failure": 4.5, "latency": 300, "tickets": 42},
    {"day": "Day 14", "conversion": 14.5, "dau": 1600, "crash_rate": 0.9, "payment_failure": 4.3, "latency": 290, "tickets": 40}
]

# 💬 B) User Feedback (30 Entries)
feedback_data = [
    "Checkout is super fast now",
    "Loved the one-click feature",
    "Finally no long forms",
    "Very convenient experience",
    "Amazing improvement",

    "Sometimes it feels slow",
    "Works fine but needs improvement",
    "Okay experience overall",
    "Not sure if payment is reliable",
    "UI is a bit confusing",

    "Payment failed twice",
    "App crashed during checkout",
    "Money deducted but no order placed",
    "Very slow after update",
    "Facing issues with payment gateway",
    "Unreliable checkout experience",
    "App freezes sometimes",
    "Too many payment failures",
    "Not trusting this feature anymore",
    "Had to retry payment multiple times",

    "Great idea but poorly executed",
    "Needs bug fixes",
    "Speed is inconsistent",
    "Checkout sometimes hangs",
    "Error messages are unclear",

    "Best feature so far",
    "Loved how quick it is",
    "Smooth when it works",
    "Good but risky",
    "Fast but unreliable"
]

# 📄 C) Release Notes / Known Issues
release_notes = {
    "feature": "1-click checkout",
    "description": "Users can place orders instantly using saved payment and address",
    "launch_day": "Day 8",
    "known_issues": [
        "Payment gateway timeout under high load",
        "Retry logic may cause duplicate transactions",
        "Increased server load causing latency spikes"
    ]
}

# Input data for the graph
input_data = {
    "metrics": metrics_data,
    "feedback": feedback_data,
    "release_notes": release_notes,
    "metrics_summary": {},
    "feedback_summary": {},
    "data_analysis": "",
    "pm_analysis": "",
    "marketing_analysis": "",
    "risk_analysis": "",
    "final_decision": {}
}
