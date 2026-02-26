feedback_store = []

def collect_feedback(user_feedback):
    feedback_store.append(user_feedback)

def improve_response():
    if feedback_store.count("helpful") > feedback_store.count("not helpful"):
        return "Response strategy is working well."
    else:
        return "Adjusting recommendations for better relevance."