# Define the chatbot responses
responses = {
    "hi": "Hello! How can I help you today?",
    "hello": "Hi there! What can I do for you?",
    "how are you": "I'm just a bot, but I'm here to help you!",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm sorry, I don't understand that."
}

# Function to get a response based on user input
def get_response(user_input):
    user_input = user_input.lower()
    return responses.get(user_input, responses["default"])

# Function to interact with the chatbot
def chat():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print("Bot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Bot: {response}")

# Start the chatbot
chat()
