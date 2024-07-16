import re

def chatbot_response(user_input):
    user_input = user_input.lower()

    
    responses = {
        "hello": "Hello! How can I help you today?",
        "hi": "Hi there! What can I do for you?",
        "how are you": "I'm just a bot, but I'm here to help you!",
        "what is your name": "I'm a simple chatbot created to assist you.",
        "bye": "Goodbye! Have a great day!",
        "thank you": "You're welcome! If you have more questions, feel free to ask.",
    }

    
    for pattern, response in responses.items():
        if re.search(r'\b' + re.escape(pattern) + r'\b', user_input):
            return response

    return "I'm sorry, I didn't understand that. Can you please rephrase?"

def main():
    print("Welcome to the Simple Chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
