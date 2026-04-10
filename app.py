from graph.workflow import build_graph
from data.mock_data import input_data
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
import json
import logging
from config.logger import setup_logger
from utils.json_parser import extract_json_from_response

# Initialize logger
logger = setup_logger(__name__)

def main():
    logger.info("=" * 60)
    logger.info("STARTING WAR ROOM PRODUCT DECISION WORKFLOW")
    logger.info("=" * 60)
    
    try:
        load_dotenv()
        logger.debug("Environment variables loaded")

        llm = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0,
            max_tokens=2000
        )
        logger.info("LLM client initialized")

        graph = build_graph(llm)
        logger.info("LangGraph workflow built")

        logger.info("[WORKFLOW] Invoking graph with initial data")
        result = graph.invoke(input_data)
        logger.info("[WORKFLOW] Graph execution completed successfully")

        # Parse and display the structured JSON output
        try:
            decision_data = extract_json_from_response(result["final_decision"])
            logger.info(f"[FINAL_DECISION] Decision: {decision_data['decision']}")
            
            print("\n" + "="*60)
            print("PRODUCT WAR ROOM DECISION")
            print("="*60)

            print(f"\n DECISION: {decision_data['decision']}")
            print(f"\n RATIONALE:\n{decision_data['rationale']}")

            print(f"\n RISK REGISTER:")
            for i, risk in enumerate(decision_data['risk_register'], 1):
                print(f"  {i}. {risk['risk']} (Impact: {risk['impact']})")
                print(f"     Mitigation: {risk['mitigation']}")

            print(f"\n ACTION PLAN (24-48 Hours):")
            for i, action in enumerate(decision_data['action_plan_24_48h'], 1):
                print(f"  {i}. {action['action']}")
                print(f"     Owner: {action['owner']} | Timeline: {action['timeline']}")

            print(f"\n COMMUNICATION PLAN:")
            print(f"  Internal: {decision_data['communication_plan']['internal']}")
            print(f"  External: {decision_data['communication_plan']['external']}")

            print(f"\n CONFIDENCE SCORE:")
            print(f"  Score: {decision_data['confidence_score']['score']}")
            print(f"  Factors to increase confidence: {decision_data['confidence_score']['factors']}")

            print("\n" + "="*60)
            
        except json.JSONDecodeError as e:
            logger.error(f"Failed to parse final decision JSON: {str(e)}", exc_info=True)
            print(f"Error parsing JSON response: {e}")
            print("Raw response:", result["final_decision"])
            
    except Exception as e:
        logger.error(f"Critical error in workflow execution: {str(e)}", exc_info=True)
        print(f"\n❌ FATAL ERROR: {str(e)}")
        raise
    
    finally:
        logger.info("=" * 60)
        logger.info("WAR ROOM WORKFLOW COMPLETED")
        logger.info("=" * 60)

if __name__ == "__main__":
    main()