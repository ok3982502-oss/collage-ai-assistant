from typing import TypedDict

class AgentState(TypedDict):
    query: str
    intent: str
    answer: str