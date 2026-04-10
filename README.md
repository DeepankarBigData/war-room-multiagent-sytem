# War Room Multi-Agent

A multi-agent decision workflow that processes product metrics, feedback, and risk signals to generate a structured war room decision.

## Setup Instructions

1. Clone the repository and open the project in VS Code.
2. Create and activate a Python virtual environment:
   ```command prompt
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```command prompt
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project root with your Groq API key:
   ```env
   GROQ_API_KEY=your_api_key_here
   ```

## How to Run End-to-End

1. Ensure your virtual environment is activated.
2. Run the application:
   ```powershell
   python app.py
   ```
3. The workflow will execute from preprocessing through decision generation, and you will see the final structured decision output.

## Example Commands

```command prompt
cd c:\projects\war_room_multiagent\war_room_multiagent
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

## Required Environment Variables

- `GROQ_API_KEY` - Your Groq API key for `langchain_groq`.

## Notes

- `app.py` loads `.env` before creating the LLM client.
- The graph starts from `graph/workflow.py` and uses `data/mock_data.py` as the initial state.
- Output is produced as a structured JSON decision result.
