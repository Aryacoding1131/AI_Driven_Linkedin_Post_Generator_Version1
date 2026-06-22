def evaluator_agent(state):

    score = 100

    if len(state["post"].split()) < 100:
        score -= 10

    if "?" not in state["post"]:
        score -= 10

    if len(state["analysis"]["keywords"]) < 3:
        score -= 5

    state["quality_score"] = score
    return state