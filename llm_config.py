from langchain_groq import ChatGroq

llm = ChatGroq(
    groq_api_key="<own API key>",
    model_name="llama-3.3-70b-versatile",
    temperature=0.7,
)
