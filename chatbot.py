import random

def run_chatbot():
    print("Hi! I'm your chatbot. Type 'bye' to exit.")

    greetings = ["Hey there!", "Hello! How's it going?", "Hi! Nice to see you."]
    how_are_you = ["I'm just code, but doing great!", "Feeling 100% functional today!", "Running smoothly, thanks for asking!"]
    name_replies = ["I'm your Python chatbot!", "You can call me PyBot.", "I'm a chatbot built by you!"]
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the function break up with the loop? It felt used.",
        "Why do Python programmers wear glasses? Because they can't C!"
    ]
    about_ai = [
        "I'm powered by simple if-elif logic — not real AI, but a good first step!",
        "Fun fact: real chatbots eventually use machine learning models to understand language.",
        "I'm a rule-based bot for now — but my creator is studying AI/ML to build smarter ones!"
    ]
    fallback = ["Sorry, I didn't understand that.", "Can you rephrase that?", "I'm not sure what you mean."]

    while True:
        user_input = input("You: ").lower()

        if user_input == "bye":
            print("Bot: Goodbye!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("Bot:", random.choice(greetings))
        elif "how are you" in user_input:
            print("Bot:", random.choice(how_are_you))
        elif "name" in user_input:
            print("Bot:", random.choice(name_replies))
        elif "joke" in user_input:
            print("Bot:", random.choice(jokes))
        elif "ai" in user_input or "machine learning" in user_input:
            print("Bot:", random.choice(about_ai))
        elif "help" in user_input:
            print("Bot: I can chat about simple things. Try saying hello, ask for a joke, or ask about AI!")
        else:
            print("Bot:", random.choice(fallback))


if __name__ == "__main__":
    run_chatbot()