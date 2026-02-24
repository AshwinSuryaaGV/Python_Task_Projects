import sys
sys.stdout.reconfigure(encoding='utf-8')
print("🤖 ChatBot: Hello! I am your assistant.")
print("Type 'exit' to end the conversation.\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("🤖 ChatBot: Goodbye! Have a great day 👋")
        break

    elif "hello" in user_input or "hi" in user_input:
        print("🤖 ChatBot: Hello there! How can I help you?")

    elif "how are you" in user_input:
        print("🤖 ChatBot: I am just a program, but I'm doing great!")

    elif "your name" in user_input:
        print("🤖 ChatBot: I am a simple Python chatbot.")

    elif "python" in user_input:
        print("🤖 ChatBot: Python is a powerful programming language!")

    elif "time" in user_input:
        import datetime
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"🤖 ChatBot: Current time is {current_time}")

    elif "bye" in user_input:
        print("🤖 ChatBot: Bye! Take care 👋")
        break

    else:
        print("🤖 ChatBot: Sorry, I don't understand that yet.")