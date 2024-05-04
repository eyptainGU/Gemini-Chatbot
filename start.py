from configparser import ConfigParser
from app import ChatBot
import sys

def main():
    config = ConfigParser()
    config.read("credentials.ini")

    api_key = config['gemini']['api_key']  # Access API key from credentials.ini file

    chatbot = ChatBot(api_key=api_key)
    chatbot.start_conversation()

    print("HI I am Genie. Ask me anything:\n ")

    while True:
        user_input = input("Genie: ")

        if user_input.lower() == "quit":
            sys.exit("Goodbye")

        try:
            response = chatbot.send_prompt(user_input)
            print(f"{chatbot.CHATBOT_NAME}: {response}")

        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()


