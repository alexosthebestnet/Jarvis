import sys
import time
import subprocess




# Print the first line
print("Welcome to Jarvis Setup\n")
time.sleep(2)

# Print the second line
print("We will ask you a few questions.\n")
time.sleep(1)

# Print the third line
print("You can answer by typing Y or N on your keyboard for yes or no\n")
time.sleep(3)

def ask_yes_no_question(question):
    while True:
        user_input = input(question + " (Y/N): ").strip().lower()
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            print("Invalid input. Please enter Y or N.\n")

def main():
    print("Lets begin.\n")
    
    if ask_yes_no_question("Are you technical with your PC?"):
        print("Great! These Skills will help\n")
    else:
        print("That's okay. It may not be for everyone. Jarvis can help\n")
    
    if ask_yes_no_question("Jarvis will be able to run code. Do you want him to be sandboxed?"):
        print("Sure Sandbox mode is now set\n")
    else:
        print("Okay. We will still add limits to keep you safe just in case.\n")
    
    if ask_yes_no_question("Have you already installed the needed packages?"):
        print("Fantastic! You can dive right in. Let's get started\n")
        
    else:
        print("Alright. We will install them now\n")
        print("Lets start with the ai system\n")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'openai'])
        print("Next lets give jarvis ears\n")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'speech_recognition'])
        print("Let me finish off with the rest...\n")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'open-interpreter'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pynput'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyttsx3'])
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'threading'])
        print("Now lets open jarvis\n")
        f = open("myfile.txt", "w")




if __name__ == "__main__":
    main()
