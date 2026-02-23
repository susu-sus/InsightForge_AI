from app.memory.state import AgentState
from app.tools.llm import LLMService


class PlannerAgent:

    def __init__(self):
        self.llm = LLMService()

    def create_plan(self, state: AgentState):

        prompt = f"""
        Break down the topic into 5 clear research sections.

        Topic: {state.query}

        Return as numbered list.
        """

        response = self.llm.generate(prompt)

        plan_steps = [
            step.strip("1234567890. ").strip()
            for step in response.split("\n")
            if step.strip()
        ]

        state.update_plan(plan_steps)

        return state