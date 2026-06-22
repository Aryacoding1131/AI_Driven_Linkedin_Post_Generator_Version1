import streamlit as st
from workflow import graph

st.set_page_config(
    page_title="AI LinkedIn Post Generator",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 AI LinkedIn Post Generator")
st.write(
    "Generate high-quality LinkedIn posts using Groq + LLMs + NLP + LangChain + LangGraph."
)

topic = st.text_area(
    "Enter your project, achievement, article, or idea:",
    height=180
)

if st.button("Generate Post"):

    if topic.strip() == "":
        st.warning("Please enter some content.")
    else:

        initial_state = {
            "user_input": topic
        }

        result = graph.invoke(initial_state)

        st.subheader("✨ LinkedIn Post")
        st.write(result["post"])

        st.subheader("🏷️ AI Generated Hashtags")
        st.write(result["hashtags"])

        st.subheader("🔑 NLP Keywords")
        st.write(", ".join(result["analysis"]["keywords"]))

        st.subheader("📊 Quality Score")
        st.progress(result["quality_score"] / 100)
        st.write(f"{result['quality_score']}/100")