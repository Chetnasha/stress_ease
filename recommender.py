def recommend(intent, sentiment):
    if intent == "academic_stress":
        return "Try the Pomodoro technique and break your study into small focused sessions."
    
    if intent == "emotional_stress":
        return "Talk to someone you trust or write down your thoughts to release emotions."
    
    if intent == "sleep_issue":
        return "Avoid screens before bed and try deep breathing for 5 minutes."
    
    if intent == "anxiety":
        return "Practice grounding techniques like 5-4-3-2-1 sensory exercise."

    if sentiment == "negative":
        return "Take a short walk, drink water, and try slow breathing."

    return "Maintain balance with regular breaks, hydration, and light exercise."