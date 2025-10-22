import speech_recognition as sr
import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Adjust speaking speed

# Start the non-blocking loop once
engine.startLoop(False)  # Non-blocking loop

def speak(text):
    """Speak text safely in Streamlit without blocking."""
    engine.say(text)
    engine.iterate()  # Non-blocking iteration

def listen_command(duration=5):
    """Listen to microphone input and return recognized text"""
    recognizer = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = recognizer.listen(source, timeout=duration)
            command = recognizer.recognize_google(audio)
            return command
    except sr.RequestError:
        print("⚠️ Could not request results from Google Speech Recognition service")
        return None
    except sr.UnknownValueError:
        print("⚠️ Could not understand audio")
        return None
    except OSError:
        print("⚠️ Microphone not found")
        return None
