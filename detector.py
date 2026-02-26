def detect_intent(text):
    text = text.lower()

    if any(word in text for word in ["exam", "study", "career", "future"]):
        return "academic_stress"
    elif any(word in text for word in ["alone", "lonely", "breakup"]):
        return "emotional_stress"
    elif any(word in text for word in ["sleep", "tired", "insomnia"]):
        return "sleep_issue"
    elif any(word in text for word in ["anxious", "panic", "fear"]):
        return "anxiety"
    else:
        return "general_stress"