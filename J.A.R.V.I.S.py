import speech_recognition as sr
import interpreter
from pynput import keyboard
import threading
import pyttsx3
import os
import time
import queue


# Initialize the TTS engine
engine = pyttsx3.init()
speech_queue = queue.Queue()

def process_speech_queue():
    """Process and speak items from the speech queue."""
    while True:
        text = speech_queue.get()
        if text is None:
            break  # Stop the thread if None is enqueued
        speak(text)

    speech_thread = threading.Thread(target=process_speech_queue, daemon=True)
    speech_thread.start()

def speak(text):
   speech_queue.put(text)


def speak(text):
    engine = pyttsx3.init()
    with tts_lock:
        engine.say(text)
        engine.runAndWait()
        engine.stop()  # Ensure the engine is stopped after speaking


# Initialize the speech recognizer
recognizer = sr.Recognizer()

# Lock for TTS engine
tts_lock = threading.Lock()
# Initialize the speech recognizer
recognizer = sr.Recognizer()

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
interpreter.api_key = "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"  # Replace with your actual API key

def display_ascii_art():
    for line in ascii_art.split('\n'):
        print(line)
        time.sleep(0.1)

def display_tutorial():
    print("Welcome to Jarvis Alpha")
    print("------------------------------------------------")
    print("1. Use the down arrow key to activate the assistant.")
    print("2. The assistant can run code on your PC.")
    print("3. You can also ask questions and get responses.")
    print("4. The assistant can browse the web for information.")
    print("------------------------------------------------")

def handle_speech():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")

        # Sending text to Open Interpreter and getting response
        interpreter.chat(text)

        if interpreter.messages:
            last_message = interpreter.messages[-1]
            if last_message['role'] == 'assistant' and 'message' in last_message:
                spoken_response = last_message['message']
                print(spoken_response)
                speak(spoken_response)
    except Exception as e:
        print(f"Error: {e}")

def on_press(key):
    if key == keyboard.Key.down:
        threading.Thread(target=handle_speech).start()

def on_release(key):
    pass  # Currently, nothing needs to happen on key release.

# Listener for keyboard events
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

# Display ASCII Art and Tutorial
display_ascii_art()
display_tutorial()

# Keep the script running
while True:
    pass
