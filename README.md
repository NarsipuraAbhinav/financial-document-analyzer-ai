### Financial Document Analyzer AI
### Overview

Brief description of what your project does.

Example:

AI-powered financial document analyzer built with CrewAI and FastAPI.
It processes uploaded financial PDFs and generates investment insights using LLM agents.

### Installation
```git clone https://github.com/<your-username>/financial-document-analyzer-ai.git```

```cd financial-document-analyzer-ai```

```python -m venv venv```

```venv\Scripts\activate```  # Windows

```pip install -r requirements.txt```

Running with Ollama (Local LLM)

```ollama pull llama3.2:3b```

```ollama run llama3.2:3b```

Then start API:

```uvicorn main:app --reload```

### API Usage
Endpoint:
POST /analyze
Form Data:

file (PDF)

query (optional)

### Debugging Notes & Common Issues

1. Changed the python version to "python 3.11"
   
2. Resolved bad dependency management design by trimming down the version pinned dependencies.

3. ImportError: Cannot import name 'Agent' from 'Crewai.agents'

   Fix: In agents.py, replace "from crewai.agents import Agent" with "from crewai import Agent". It is due to usage of new version

4. ImportError: Cannot import name 'SerperDevTool'
   
   Fix: In tools.py, Update import according to new version.

5. NameError: name "llm" is not defined
   
   Fix: In agents.py, change "llm=llm" to "llm = LLM(model="ollama/tinyllama", base_url="http://localhost:11434")"

## API Issues

1. Error: "detail": "Error processing financial document: 'function' object has no attribute 'get'"

   Issue: The error occurred because a plain Python function was being passed as a tool to CrewAI's Task.

   Fix: Replace "tools=[FinancialDocumentTool.read_data_tool]" with "tools=[FinancialDocumentTool()]"

3. Error: Unexpected Internal Server Error / Runtime Conflict

   Issue: Both the CrewAI task and the FastAPI endpoint function were defined with the same name: analyze_financial_document

   Python does not allow two different objects with the same name in the same namespace without overwriting one.

   Fix: Rename the task in task.py as "financial_analysis_task = Task(...)"

### Sample Output

<img width="1898" height="964" alt="Screenshot 2026-02-27 024518" src="https://github.com/user-attachments/assets/0c8c6420-87e8-4d32-bb8c-71bb72d05866" />
