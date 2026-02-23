from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self):
        self.model = SentenceTransformer("all-mpnet-base-v2")

    def embed_text(self, text: str):
        vector = self.model.encode(text)
        return vector.tolist()