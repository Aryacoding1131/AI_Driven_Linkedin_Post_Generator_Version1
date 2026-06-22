from agents.llm_config import llm

def rewrite_agent(state):

    prompt = f"""
Improve the following LinkedIn post.
Make it more engaging, polished, and professional.

Post:
{state['post']}
"""

    response = llm.invoke(prompt)
    state["post"] = response.content

    return state