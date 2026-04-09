from graph.workflow import build_graph
from data.mock_data import input_data
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import json

load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    max_tokens=2000  # Increased for detailed JSON output
)

graph = build_graph(llm)

result = graph.invoke(input_data)

# Parse and display the structured JSON output
try:
    decision_data = json.loads(result["final_decision"])
    print("\n" + "="*60)
    print("🚀 PRODUCT WAR ROOM DECISION")
    print("="*60)

    print(f"\n📊 DECISION: {decision_data['decision']}")
    print(f"\n📋 RATIONALE:\n{decision_data['rationale']}")

    print(f"\n⚠️  RISK REGISTER:")
    for i, risk in enumerate(decision_data['risk_register'], 1):
        print(f"  {i}. {risk['risk']} (Impact: {risk['impact']})")
        print(f"     Mitigation: {risk['mitigation']}")

    print(f"\n⏰ ACTION PLAN (24-48 Hours):")
    for i, action in enumerate(decision_data['action_plan_24_48h'], 1):
        print(f"  {i}. {action['action']}")
        print(f"     Owner: {action['owner']} | Timeline: {action['timeline']}")

    print(f"\n📢 COMMUNICATION PLAN:")
    print(f"  Internal: {decision_data['communication_plan']['internal']}")
    print(f"  External: {decision_data['communication_plan']['external']}")

    print(f"\n🎯 CONFIDENCE SCORE:")
    print(f"  Score: {decision_data['confidence_score']['score']}")
    print(f"  Factors to increase confidence: {decision_data['confidence_score']['factors']}")

    print("\n" + "="*60)

except json.JSONDecodeError as e:
    print(f"Error parsing JSON response: {e}")
    print("Raw response:", result["final_decision"])