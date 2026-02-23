from app.memory.state import AgentState
from app.tools.llm import LLMService
from app.tools.retriever import Retriever
from app.tools.embeddings import EmbeddingService


class ResearchAgent:

    def __init__(self):
        self.llm = LLMService()

        embedder = EmbeddingService()
        sample_vector = embedder.embed_text("dimension check")
        dimension = len(sample_vector)

        self.retriever = Retriever(dimension)

    def conduct_research(self, state: AgentState):

        for step in state.plan:

            retrieved_docs = self.retriever.retrieve(step)
            context = "\n".join(retrieved_docs)

            prompt = f"""
            Write a detailed explanation about:

            {step}

            Use this context if useful:
            {context}
            """

            content = self.llm.generate(prompt)

            state.add_research(f"{step}\n{content}")

        return state