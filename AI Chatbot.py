import pyttsx3
from datetime import datetime

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define a function to speak text
def speak(text):
    print("AI Bot:",text)
    engine.say(text)
    engine.runAndWait()


# greet
print("\nOliver: Hello! I am Python AI assistant. Type 'exit' to end.\n")

# Start chatting loop
while True:
    user_input = input("👤 You: ").lower().strip()

    if user_input in ["hi", "hello", "hey"]:
        speak("Hello! I am Oliver. How may I assist you today?")

    elif "how are you" in user_input:
        speak("I am just a code, but I feel awesome helping you.")

    elif "name" in user_input:
        speak("I am Oliver, your AI assistant.")

    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")

    # Calculate
    elif "calculate" in user_input:
        try:
            result = eval(user_input.replace("calculate", ""))
            speak(f"The result is: {result}")
        except:
            speak("Sorry! I couldn't understand the calculation.")

    elif "bye" in user_input:
        speak("Good bye! See you soon.\n")
        break

    else: 
        speak("Sorry I couldn't understand that.")

