import pyttsx3

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# Call on start
speak("Hello, I am Jarvis. How can I assist you today?")
