from langgraph.graph import StateGraph, END

from state import AgentState

from intent_agent import classify_intent
from admission_agent import admission_agent
from exam_agent import exam_agent
from fees_agent import fees_agent
from scholarship_agent import scholarship_agent
from department_agent import department_agent


# Intent Node
def intent_node(state: AgentState):
    intent = classify_intent(state["query"])
    state["intent"] = intent
    return state


# Admission Node
def admission_node(state: AgentState):
    state["answer"] = admission_agent(state["query"])
    return state


# Exam Node
def exam_node(state: AgentState):
    state["answer"] = exam_agent(state["query"])
    return state


# Fees Node
def fees_node(state: AgentState):
    state["answer"] = fees_agent(state["query"])
    return state


# Scholarship Node
def scholarship_node(state: AgentState):
    state["answer"] = scholarship_agent(state["query"])
    return state


# Department Node
def department_node(state: AgentState):
    state["answer"] = department_agent(state["query"])
    return state


# Router
def route(state: AgentState):

    intent = state["intent"].lower()

    if "admission" in intent:
        return "admission"

    elif "exam" in intent:
        return "exam"

    elif "fees" in intent:
        return "fees"

    elif "scholarship" in intent:
        return "scholarship"

    elif "department" in intent:
        return "department"

    return END


# Build Graph
builder = StateGraph(AgentState)

builder.add_node("intent", intent_node)
builder.add_node("admission", admission_node)
builder.add_node("exam", exam_node)
builder.add_node("fees", fees_node)
builder.add_node("scholarship", scholarship_node)
builder.add_node("department", department_node)

builder.set_entry_point("intent")

builder.add_conditional_edges(
    "intent",
    route,
    {
        "admission": "admission",
        "exam": "exam",
        "fees": "fees",
        "scholarship": "scholarship",
        "department": "department",
        END: END,
    },
)

builder.add_edge("admission", END)
builder.add_edge("exam", END)
builder.add_edge("fees", END)
builder.add_edge("scholarship", END)
builder.add_edge("department", END)

graph = builder.compile()