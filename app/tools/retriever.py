from app.tools.embeddings import EmbeddingService
from app.tools.vector_store import VectorStore
from app.utils.logger import setup_logger


logger = setup_logger("retriever")


class Retriever:
    def __init__(self, dimension: int):
        self.embedder = EmbeddingService()
        self.vector_store = VectorStore(dimension)
        self.vector_store.load()

    # -----------------------------
    # Add document to vector store
    # -----------------------------
    def add_document(self, text: str):
        logger.info("Adding document through retriever...")
        vector = self.embedder.embed_text(text)
        self.vector_store.add(vector, text)
        self.vector_store.save()

    # -----------------------------
    # Retrieve relevant documents
    # -----------------------------
    def retrieve(self, query: str, top_k=3):
        logger.info("Retrieving documents...")

        query_vector = self.embedder.embed_text(query)
        results = self.vector_store.search(query_vector, top_k=top_k)

        logger.info("Documents retrieved successfully.")
        return results