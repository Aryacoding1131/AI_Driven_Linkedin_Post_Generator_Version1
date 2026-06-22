from agents.llm_config import llm

def hashtag_agent(state):

    prompt = f"""
Generate exactly 8 relevant LinkedIn hashtags for the following post.

Post:
{state['post']}

Return only hashtags separated by spaces.
"""

    response = llm.invoke(prompt)

    state["hashtags"] = response.content
    return state