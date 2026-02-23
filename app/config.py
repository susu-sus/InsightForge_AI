import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ==============================
# 🔑 API CONFIGURATION
# ==============================

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")




# ==============================
# 🤖 MODEL CONFIGURATION
# ==============================
LLM_MODEL = "llama3-8b-8192"

EMBEDDING_MODEL = "text-embedding-3-small"


# ==============================
# 📁 VECTOR STORE CONFIG
# ==============================

VECTOR_STORE_PATH = "data/vector_store"


# ==============================
# ⚙️ SYSTEM SETTINGS
# ==============================

MAX_TOKENS = 1000
TEMPERATURE = 0.3