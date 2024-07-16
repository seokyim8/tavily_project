from typing import List, TypedDict

class AgentState(TypedDict):
    query: str
    collected: List[dict]
    images: List[str]
    reviews: list[dict]
    html: str