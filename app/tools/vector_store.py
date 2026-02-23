import os
import faiss
import numpy as np
import pickle

from app.config import VECTOR_STORE_PATH
from app.utils.logger import setup_logger

logger = setup_logger("vector_store")


class VectorStore:
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.texts = []

        os.makedirs(VECTOR_STORE_PATH, exist_ok=True)

        self.index_path = os.path.join(VECTOR_STORE_PATH, "faiss.index")
        self.texts_path = os.path.join(VECTOR_STORE_PATH, "texts.pkl")

    # -------------------------
    # Add new document
    # -------------------------
    def add(self, vector, text: str):
        logger.info("Adding vector to store...")

        vector = np.array([vector]).astype("float32")
        self.index.add(vector)
        self.texts.append(text)

        logger.info("Vector added successfully.")

    # -------------------------
    # Search similar vectors
    # -------------------------
    def search(self, query_vector, top_k=3):

        if self.index.ntotal == 0:
            return []

        query_vector = np.array([query_vector]).astype("float32")

        distances, indices = self.index.search(query_vector, top_k)

        results = []

        for idx in indices[0]:
            if 0 <= idx < len(self.texts):
                results.append(self.texts[idx])

        return results
    # -------------------------
    # Save index to disk
    # -------------------------
    def save(self):
        faiss.write_index(self.index, self.index_path)

        with open(self.texts_path, "wb") as f:
            pickle.dump(self.texts, f)

        logger.info("Vector store saved.")

    # -------------------------
    # Load index from disk
    # -------------------------
    def load(self):
        if os.path.exists(self.index_path):
            self.index = faiss.read_index(self.index_path)

            with open(self.texts_path, "rb") as f:
                self.texts = pickle.load(f)

            logger.info("Vector store loaded.")