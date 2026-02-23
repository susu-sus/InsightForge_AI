from app.memory.state import AgentState
from app.tools.llm import LLMService


class StrategyAgent:

    def __init__(self):
        self.llm = LLMService()

    def generate_final_report(self, state: AgentState):

        combined = "\n\n".join(state.research_findings)

        # Safety truncation
        combined = combined[:3500]

        prompt = f"""
        Create a structured final research report.

        Include:
        - Executive Summary
        - Key Insights
        - Conclusion

        Research content:
        {combined}
        """

        final_report = self.llm.generate(prompt, max_tokens=600)

        state.set_final_report(final_report)

        return state