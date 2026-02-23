from typing import List, Dict, Any


class AgentState:
    """
    Shared memory state across all agents.
    """

    def __init__(self, query: str):
        self.query: str = query
        self.plan: List[str] = []
        self.research_findings: List[str] = []
        self.final_report: str = ""
        self.metadata: Dict[str, Any] = {}

    # ----------------------------
    # Planner updates plan
    # ----------------------------
    def update_plan(self, plan_steps: List[str]):
        self.plan = plan_steps

    # ----------------------------
    # Research agent adds findings
    # ----------------------------
    def add_research(self, content: str):
        self.research_findings.append(content)

    # ----------------------------
    # Strategy agent sets final report
    # ----------------------------
    def set_final_report(self, report: str):
        self.final_report = report

    # ----------------------------
    # Utility: view state
    # ----------------------------
    def to_dict(self):
        return {
            "query": self.query,
            "plan": self.plan,
            "research_findings": self.research_findings,
            "final_report": self.final_report,
            "metadata": self.metadata,
        }