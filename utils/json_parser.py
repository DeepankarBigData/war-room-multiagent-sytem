import json
import logging

logger = logging.getLogger(__name__)


def extract_json_from_response(response_text):
    """
    Extract JSON from LLM response, handling markdown code blocks.
    
    Args:
        response_text: Raw LLM response that may contain markdown-wrapped JSON
        
    Returns:
        dict: Parsed JSON object
        
    Raises:
        json.JSONDecodeError: If JSON parsing fails
    """
    if not response_text or not isinstance(response_text, str):
        logger.error(f"Invalid response text: {response_text}")
        raise ValueError("Response text must be a non-empty string")
    
    # Try to extract from markdown code blocks
    if "```json" in response_text:
        logger.debug("Extracting JSON from ```json code block")
        start = response_text.find("```json") + 7
        end = response_text.find("```", start)
        json_str = response_text[start:end].strip()
    elif "```" in response_text:
        logger.debug("Extracting JSON from generic ``` code block")
        start = response_text.find("```") + 3
        end = response_text.find("```", start)
        json_str = response_text[start:end].strip()
    else:
        json_str = response_text.strip()
    
    logger.debug(f"Attempting to parse extracted JSON (first 150 chars): {json_str[:150]}")
    
    try:
        parsed = json.loads(json_str)
        logger.debug(f"Successfully parsed JSON with keys: {list(parsed.keys()) if isinstance(parsed, dict) else 'array'}")
        return parsed
    except json.JSONDecodeError as e:
        logger.error(f"Failed to parse JSON: {str(e)}")
        logger.error(f"JSON string (first 500 chars): {json_str[:500]}")
        raise
