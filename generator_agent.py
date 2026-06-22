from langchain_core.prompts import PromptTemplate
from agents.llm_config import llm

prompt = PromptTemplate(
    input_variables=["topic", "keywords"],
    template="""
You are an expert LinkedIn content creator.

Generate a professional and engaging LinkedIn post.

Topic:
{topic}

Important keywords:
{keywords}

Instructions:
1. Write around 150-180 words.
2. Use a friendly and professional tone.
3. Start with an attention-grabbing opening.
4. Explain the achievement or idea clearly.
5. End with a discussion question.
6. Do not generate hashtags.
"""
)

chain = prompt | llm

def generator_agent(state):
    response = chain.invoke({
        "topic": state["user_input"],
        "keywords": ", ".join(state["analysis"]["keywords"])
    })

    state["post"] = response.content
    return state