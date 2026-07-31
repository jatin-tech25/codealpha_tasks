print("🤖 Chatbot: Hello! I'm your basic chatbot.")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "hello" or user_input == "hi":
        print("Bot: Hello! How are you?")

    elif user_input == "how are you":
        print("Bot: I'm doing great! Thanks for asking.")

    elif user_input == "what is your name":
        print("Bot: My name is Python Chatbot.")

    elif user_input == "what can you do":
        print("Bot: I can have a simple conversation with you.")

    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day 😊")
        break

    else:
        print("Bot: Sorry, I don't understand that.")
        print("Bot:. Thanks ")
