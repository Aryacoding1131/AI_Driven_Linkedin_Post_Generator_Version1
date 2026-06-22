from nlp.preprocess import analyze_text

def input_agent(state):
    analysis = analyze_text(state["user_input"])
    state["analysis"] = analysis
    return state