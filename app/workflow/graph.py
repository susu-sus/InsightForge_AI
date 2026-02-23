from app.memory.state import AgentState
from app.agents.planner_agent import PlannerAgent
from app.agents.research_agent import ResearchAgent
from app.agents.strategy_agent import StrategyAgent
from app.utils.logger import setup_logger


logger = setup_logger("workflow_graph")


class ResearchWorkflow:

    def __init__(self):
        self.planner = PlannerAgent()
        self.researcher = ResearchAgent()
        self.strategist = StrategyAgent()

    def run(self, query: str) -> AgentState:
        logger.info("Workflow started.")

        # Initialize shared state
        state = AgentState(query)

        # Step 1: Planning
        state = self.planner.create_plan(state)

        # Step 2: Research
        state = self.researcher.conduct_research(state)

        # Step 3: Strategy synthesis
        state = self.strategist.generate_final_report(state)

        logger.info("Workflow completed successfully.")

        return state