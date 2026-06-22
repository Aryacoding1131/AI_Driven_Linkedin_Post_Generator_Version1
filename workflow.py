from typing import TypedDict
from langgraph.graph import StateGraph, END

from agents.input_agent import input_agent
from agents.generator_agent import generator_agent
from agents.hashtag_agent import hashtag_agent
from agents.evaluator_agent import evaluator_agent
from agents.rewrite_agent import rewrite_agent


class GraphState(TypedDict):
    user_input: str
    analysis: dict
    post: str
    hashtags: str
    quality_score: int


builder = StateGraph(GraphState)

builder.add_node("InputAgent", input_agent)
builder.add_node("GeneratorAgent", generator_agent)
builder.add_node("HashtagAgent", hashtag_agent)
builder.add_node("EvaluatorAgent", evaluator_agent)
builder.add_node("RewriteAgent", rewrite_agent)

builder.set_entry_point("InputAgent")

builder.add_edge("InputAgent", "GeneratorAgent")
builder.add_edge("GeneratorAgent", "HashtagAgent")
builder.add_edge("HashtagAgent", "EvaluatorAgent")


def quality_router(state):
    if state["quality_score"] < 85:
        return "RewriteAgent"
    return END


builder.add_conditional_edges(
    "EvaluatorAgent",
    quality_router,
    {
        "RewriteAgent": "RewriteAgent",
        END: END
    }
)

builder.add_edge("RewriteAgent", "HashtagAgent")

graph = builder.compile()