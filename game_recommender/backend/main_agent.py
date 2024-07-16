from langgraph.graph import StateGraph
from .agents.state import AgentState
from .agents.collector_agent import CollectorAgent
from .agents.selector_agent import SelectorAgent
from .agents.publisher_agent import PublisherAgent


class Main_Agent:
    def __init__(self, query="fps_games"):
        self.query = query

        # Initialize agents
        collector_agent = CollectorAgent()
        selector_agent = SelectorAgent()
        publisher_agent = PublisherAgent()

        # Create graph
        graph = StateGraph(AgentState)
        graph.add_node("collector", collector_agent.run)
        graph.add_node("selector", selector_agent.run)
        graph.add_node("publisher", publisher_agent.run)
        graph.add_edge("collector", "selector")
        graph.add_edge("selector", "publisher")

        # Set up entry and ending points
        graph.set_entry_point("collector")
        graph.set_finish_point("publisher")

        self.graph = graph.compile()
    
    def run(self):
        result = self.graph.invoke({"query": "Games with the following: " + self.query})
        return result  
