def generate_prompt(user_input, intent, sentiment):
    prompt = f"""
    User is feeling {sentiment}.
    Detected intent: {intent}.
    User says: "{user_input}"

    Respond empathetically and give a short stress relief suggestion.
    """
    return prompt