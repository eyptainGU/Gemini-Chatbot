from configparser import ConfigParser
from app import ChatBot
import sys
import time
import threading

# variable to control the loading animation thread
stop_loading = False

def main():
    config = ConfigParser()
    config.read("credentials.ini")

    api_key = config['gemini']['api_key']

    chatbot = ChatBot(api_key=api_key)
    chatbot.start_conversation()

    print("HI I am Genie. Ask me anything:\n ")

    while True:
        user_input = input("Genie: ")

        if user_input.lower() == "quit":
            sys.exit("Goodbye")

        try:
            # Reset the stop_loading flag for each new request
            global stop_loading
            stop_loading = False
            
            # Create a separate thread for the loading animation
            loading_thread = threading.Thread(target=loading_animation)
            loading_thread.start()

            
            response = chatbot.process_question(user_input, "bash")

            # Stop the loading animation thread
            stop_loading = True
            loading_thread.join()

        
            print(f"{chatbot.CHATBOT_NAME}: {response}")

        except Exception as e:
            # Stop the loading animation thread on error
            stop_loading = True
            loading_thread.join()
            print(f"Error: {e}")

def loading_animation():
    while not stop_loading:
        for char in '|/-\\':
            sys.stdout.write('\rLoading ' + char)
            sys.stdout.flush()
            time.sleep(0.1)
    # Clear the loading animation when stopped
    sys.stdout.write('\r' + ' ' * 10 + '\r')
    sys.stdout.flush()

if __name__ == "__main__":
    main()

