🧠 InsightForge AI
Agentic Multi-Agent Research Intelligence Platform

InsightForge AI is a modular, multi-agent research intelligence system that transforms natural language queries into structured, analytical reports using Retrieval-Augmented Generation (RAG) and agent-based orchestration.

Rather than acting as a simple chatbot, the system decomposes problems, retrieves relevant context, performs structured reasoning, and generates professional research outputs.

🚀 What This Project Demonstrates

Multi-agent AI architecture

Task decomposition and orchestration

Retrieval-Augmented Generation (RAG)

Vector-based semantic search (FAISS)

Structured analytical output generation

Modular, scalable system design

Production-style UI integration

🏗 System Architecture

InsightForge AI follows an agent-based execution pipeline:

User Query
→ Planner Agent (breaks query into structured research steps)
→ Research Agent (retrieves context using vector similarity search + LLM reasoning)
→ Strategy Agent (refines and structures analytical insights)
→ Report Engine (generates professional output)

This architecture separates reasoning responsibilities, making the system modular and extensible.

🧩 Core Components
🔹 Agents Layer (app/agents)

planner_agent.py – Task decomposition

research_agent.py – Context retrieval + LLM interaction

strategy_agent.py – Structured insight generation

🔹 Tools Layer (app/tools)

embeddings.py – Semantic vector generation

vector_store.py – FAISS indexing and similarity search

retriever.py – Context retrieval pipeline

llm.py – LLM API integration

🔹 Workflow Layer (app/workflow)

graph.py – Orchestrates multi-agent execution

🔹 Memory Layer (app/memory)

state.py – Shared execution state across agents

🔹 UI Layer (ui/)

streamlit_app.py – Interactive interface

style.css – Custom SaaS-style UI

hero.html – Structured landing layout

📁 Project Structure

InsightForge-AI/
│
├── app/
│   ├── agents/
│   │   ├── planner_agent.py       # Decomposes research query into structured steps
│   │   ├── research_agent.py      # Performs RAG-based retrieval & contextual reasoning
│   │   └── strategy_agent.py      # Synthesizes and structures final analytical output
│   │
│   ├── tools/
│   │   ├── embeddings.py          # Semantic vector generation (SentenceTransformers)
│   │   ├── vector_store.py        # FAISS-based vector indexing & similarity search
│   │   ├── retriever.py           # Context retrieval pipeline
│   │   └── llm.py                 # LLM API integration (Groq)
│   │
│   ├── memory/
│   │   └── state.py               # Shared state object across agent pipeline
│   │
│   ├── workflow/
│   │   └── graph.py               # Multi-agent execution orchestration
│   │
│   ├── utils/
│   │   └── logger.py              # Centralized logging system
│   │
│   └── config.py                  # Environment & model configuration
│
├── data/
│   └── logs/
│       └── system.log             # Runtime logs
│
├── ui/
│   ├── static/
│   │   ├── hero.html              # Landing page structure
│   │   └── style.css              # Custom SaaS-style UI
│   │
│   └── streamlit_app.py           # Streamlit application entry point
│
├── requirements.txt
├── .env
└── README.md

🧠 How It Works

User enters a research topic.

Planner Agent decomposes the topic into structured research steps.

Research Agent retrieves semantically relevant information using vector similarity search.

Strategy Agent synthesizes and organizes insights.

The system produces structured research output ready for presentation or documentation.

🛠 Technologies Used

Python

Streamlit

FAISS (Vector Database)

SentenceTransformers

Groq LLM API

ReportLab

python-pptx

⚙️ Installation
git clone https://github.com/yourusername/InsightForge-AI.git
cd InsightForge-AI
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

Create a .env file:

GROQ_API_KEY=your_api_key_here

Run the application:

streamlit run ui/streamlit_app.py
📄 Output Capabilities

The system generates:

Structured research analysis

Professional PDF reports

Executive PowerPoint presentations

🎯 Engineering Focus

This project emphasizes:

Agent-based AI design

Separation of reasoning responsibilities

RAG-based context injection

Modular architecture for scalability

Real-world report automation

🚀 Future Enhancements

Persistent document ingestion pipeline

API deployment with FastAPI

Streaming LLM responses

Role-based user access

Frontend migration to React

👩‍💻 Author

Suvarna S P
AI & Data Science Enthusiast
Focused on building structured, agentic AI systems.