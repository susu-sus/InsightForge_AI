# 🧠 InsightForge AI  
### Agentic Multi-Agent Research Intelligence Platform

InsightForge AI is a modular, multi-agent research intelligence system that transforms natural language queries into structured analytical reports using Retrieval-Augmented Generation (RAG) and agent-based orchestration.

Rather than acting as a simple chatbot, the system decomposes problems, retrieves relevant context, performs structured reasoning, and generates professional research outputs.

---

## 🚀 What This Project Demonstrates

- Multi-agent AI architecture  
- Task decomposition and orchestration  
- Retrieval-Augmented Generation (RAG)  
- Vector-based semantic search (FAISS)  
- Structured analytical output generation  
- Modular, scalable system design  
- Production-style UI integration  

---

## 🏗 System Architecture

InsightForge AI follows an agent-based execution pipeline:

```
User Query
   ↓
Planner Agent (task decomposition)
   ↓
Research Agent (vector retrieval + LLM reasoning)
   ↓
Strategy Agent (structured synthesis)
   ↓
Report Engine (PDF / PPT generation)
```

This architecture separates reasoning responsibilities, making the system modular and extensible.

---

## 🧩 Core Components

### 🔹 Agents Layer (`app/agents`)
- `planner_agent.py` – Task decomposition  
- `research_agent.py` – Context retrieval + LLM interaction  
- `strategy_agent.py` – Structured insight generation  

### 🔹 Tools Layer (`app/tools`)
- `embeddings.py` – Semantic vector generation  
- `vector_store.py` – FAISS similarity search  
- `retriever.py` – Context retrieval pipeline  
- `llm.py` – LLM API integration  

### 🔹 Workflow Layer (`app/workflow`)
- `graph.py` – Multi-agent execution orchestration  

### 🔹 Memory Layer (`app/memory`)
- `state.py` – Shared execution state  

### 🔹 UI Layer (`ui/`)
- `streamlit_app.py` – Interactive interface  
- `style.css` – Custom SaaS-style UI  
- `hero.html` – Structured landing layout  

---

## 📁 Project Structure

```
InsightForge-AI/
│
├── app/
│   ├── agents/
│   │   ├── planner_agent.py
│   │   ├── research_agent.py
│   │   └── strategy_agent.py
│   │
│   ├── tools/
│   │   ├── embeddings.py
│   │   ├── vector_store.py
│   │   ├── retriever.py
│   │   └── llm.py
│   │
│   ├── memory/
│   │   └── state.py
│   │
│   ├── workflow/
│   │   └── graph.py
│   │
│   ├── utils/
│   │   └── logger.py
│   │
│   └── config.py
│
├── data/
│   └── logs/
│       └── system.log
│
├── ui/
│   ├── static/
│   │   ├── hero.html
│   │   └── style.css
│   │
│   └── streamlit_app.py
│
├── requirements.txt
├── .env (local only – not pushed)
└── README.md
```

---

## 🧠 How It Works

1. User enters a research topic.  
2. Planner Agent decomposes it into structured steps.  
3. Research Agent retrieves semantically relevant information using vector similarity search.  
4. Strategy Agent synthesizes and organizes insights.  
5. The system produces structured research output ready for presentation or documentation.  

---

## 🛠 Technologies Used

- Python  
- Streamlit  
- FAISS  
- SentenceTransformers  
- Groq LLM API  
- ReportLab  
- python-pptx  

---

## ⚙️ Installation

```bash
git clone https://github.com/susu-sus/InsightForge_AI.git
cd InsightForge_AI
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run ui/streamlit_app.py
```

---

## 📄 Output Capabilities

The system generates:

- Structured research analysis  
- Professional PDF reports  
- Executive PowerPoint presentations  

---

## 🎯 Engineering Focus

- Agent-based AI design  
- Separation of reasoning responsibilities  
- RAG-based context injection  
- Modular architecture for scalability  
- Real-world report automation  

---

## 🚀 Future Enhancements

- Persistent document ingestion pipeline  
- API deployment with FastAPI  
- Streaming LLM responses  
- Role-based user access  
- Frontend migration to React  

---

## 👩‍💻 Author

**Suvarna S P**  
AI & Data Science Enthusiast  
Focused on building structured, agentic AI systems.
