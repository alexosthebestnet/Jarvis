import interpreter
import os
import time

# ASCII Art
ascii_art = """
    d88b  .d8b.  d8888b. db    db d888888b .d8888. 
   `8P' d8' `8b 88  `8D 88    88   `88'   88'  YP 
    88  88ooo88 88oobY' Y8    8P    88    `8bo.   
    88  88~~~88 88`8b   `8b  d8'    88      `Y8b. 
db. 88  88   88 88 `88.  `8bd8'    .88.   db   8D 
Y8888P  YP   YP 88   YD    YP    Y888888P `8888Y' 
"""

# Custom system message and model configuration
interpreter.system_message += "\nRun all shell commands with -y."
interpreter.model = "gpt-3.5-turbo"
interpreter.auto_run = True  # Don't require user confirmation
interpreter.api_key = "sk-000"  # Replace with your actual API key

API_KEY_FILE = "api_key.txt"

# Modified part for handling API key
def get_api_key():
    # Check if API key file exists
    if os.path.exists(API_KEY_FILE):
        with open(API_KEY_FILE, 'r') as file:
            return file.read().strip()
    else:
        # Ask user for API key
        api_key = input("Please enter your API key: ")
        with open(API_KEY_FILE, 'w') as file:
            file.write(api_key)
        return api_key

# Set API key for interpreter
interpreter.api_key = get_api_key()

def display_ascii_art():
    for line in ascii_art.split('\n'):
        print(line)
        time.sleep(0.1)

def display_tutorial():
    print("Welcome to Jarvis Alpha")
    print("------------------------------------------------")
    print("1. Type your commands or questions and press Enter.")
    print("2. The assistant can run code on your PC.")
    print("3. The assistant can browse the web for information.")
    print("------------------------------------------------")

def handle_text_input():
    while True:
        text = input("Type your command or question: ")

        # Sending text to Open Interpreter and getting response
        interpreter.chat(text)

        if interpreter.messages:
            last_message = interpreter.messages[-1]
            if last_message['role'] == 'assistant' and 'message' in last_message:
                response = last_message['message']
                print(response)

# Display ASCII Art and Tutorial
display_ascii_art()
display_tutorial()

# Start handling text input
handle_text_input()
