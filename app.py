from sentiment import analyze_sentiment
from detector import detect_intent
from recommender import recommend
from prompts import generate_prompt
from feedback import collect_feedback, improve_response

def main():
    print("🧠 Stress Ease for Youth – AI Wellness Assistant")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        sentiment = analyze_sentiment(user_input)
        intent = detect_intent(user_input)

        response = recommend(intent, sentiment)
        prompt_used = generate_prompt(user_input, intent, sentiment)

        print("\nAI Response:", response)
        print("\n[Prompt Used]", prompt_used)

        feedback = input("\nWas this helpful? (helpful/not helpful): ")
        collect_feedback(feedback)

        print(improve_response())
        print("-" * 50)

if __name__ == "__main__":
    main()