import pyttsx3
import subprocess
import speech_recognition as sr

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=10)
        print("Recognizing...")

    try:
        user_response = recognizer.recognize_google(audio).lower()
        print("You said:", user_response)
        return user_response
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand what you said.")
        return ""
    except sr.RequestError as e:
        print("Sorry, I encountered an error while processing your request:", str(e))
        return ""

def main():
    # Greet the user
    speak("Hello sir, welcome back!")

    # Ask for permission
    speak("Shall I enable my main AI system for today?")

    # Possible responses for "yes" and "no"
    valid_yes_responses = ["yes", "sure", "okay", "absolutely", "affirmative", "certainly", "indeed", "of course", "please do", "do it"]
    valid_no_responses = ["no", "not today", "not now", "negative", "nope", "sorry", "nah", "never", "I'm good", "stop"]

    user_response = ""
    while user_response == "":
        user_response = recognize_speech()

    if user_response in valid_yes_responses:
        # Launch the file (replace 'file_path' with your desired file)
        file_path = "path/to/your/file.txt"
        try:
            subprocess.Popen(["xdg-open", file_path])  # Linux
        except Exception:
            speak("Could not open the file. Please check the file path or your operating system.")
    elif user_response in valid_no_responses:
        # Perform an alternative action (you can replace this as needed)
        speak("Okay, maybe next time.")
    else:
        speak("I'm sorry, I didn't understand your response.")

if __name__ == "__main__":
    main()
