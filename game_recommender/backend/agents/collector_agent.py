from tavily import TavilyClient
from .state import AgentState
from .env import TAVILY_API_KEY


class CollectorAgent:
    def __init__(self):
        self.tavily_client = TavilyClient(api_key=TAVILY_API_KEY)

    def search_for_game(self, query: str)->list:
        '''
        Collecting game-related sources. Returns the search results.
        '''
        search_result = self.tavily_client.search(query=query, max_results=3)
        return search_result["results"]
    
    def search_for_images(self, games: list[str])->list[str]:
        '''
        Looks up corresponding images to the games provided. Returns a list of URLs to images.
        '''
        images = []
        for game in games:
            search_result = self.tavily_client.search(query=game, topic="general", max_results=1, include_images=True)
            images.append(search_result["images"][0])
        return images

    def run(self, state: AgentState):
        '''
        Combines the Tavily search result and saves it as part of the state.
        '''
        results = self.search_for_game(state["query"])
        images = self.search_for_images(map(lambda x: x["title"], results))
        return {"collected": results, "images": images}
    
