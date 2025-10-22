from gtts import gTTS
import base64
import tempfile
import streamlit as st

def speak(text):
    """
    Converts text to speech and plays it automatically in Streamlit.
    """
    tts = gTTS(text=text, lang="en")
    
    # Save to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts.save(fp.name)
        audio_file_path = fp.name

    # Streamlit audio player (auto-play)
    audio_bytes = open(audio_file_path, "rb").read()
    st.audio(audio_bytes, format="audio/mp3", start_time=0)
