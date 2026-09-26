# CodeAlpha - Basic Chatbot

def chatbot():
    print("===== Basic Chatbot =====")
    print("Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "hello" or user_input == "hi":
            print("Bot: Hi! Nice to meet you.")

        elif user_input == "how are you":
            print("Bot: I'm fine, thanks! How are you?")

        elif user_input == "what is your name":
            print("Bot: I'm a simple Python chatbot.")

        elif user_input == "what can you do":
            print("Bot: I can respond to simple messages.")

        elif user_input == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")


chatbot()
