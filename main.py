import streamlit as st
from modules import intents, system_control, voice, animation
import time

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(page_title="Ultimate Real-Time Jarvis", layout="wide", page_icon="🤖")
st.title("🦾 Ultimate Jarvis AI - Real Time")

# ---------------------------
# Sidebar: History
# ---------------------------
if "recent_commands" not in st.session_state:
    st.session_state["recent_commands"] = []

st.sidebar.title("🗂️ Temp & History")
if st.sidebar.button("Clear History"):
    st.session_state["recent_commands"] = []

# Display recent commands
for cmd in st.session_state["recent_commands"]:
    st.sidebar.write(f"- {cmd}")

# ---------------------------
# Load intents
# ---------------------------
all_intents = intents.load_intents()

# ---------------------------
# Animated Jarvis Startup
# ---------------------------
animation.jarvis_ui("idle")
st.subheader("Hello, I am Jarvis. How can I assist you today?")
voice.speak("Hello, I am Jarvis. How can I assist you today?")

# ---------------------------
# Command Input
# ---------------------------
audio_text = st.text_input("Type your command here:")

if audio_text:
    st.write(f"**You said:** {audio_text}")
    st.session_state["recent_commands"].append(audio_text)

    animation.jarvis_ui("processing")
    time.sleep(0.5)

    # Match intent
    matched_intent = intents.match_intent(all_intents, audio_text)
    if matched_intent:
        response = matched_intent["responses"][0]
        st.success(f"**Jarvis:** {response}")
        voice.speak(response)
        animation.jarvis_ui("speaking")

        # System commands
        if matched_intent["tag"] == "open_app":
            system_control.open_application(audio_text)
        elif matched_intent["tag"] == "send_email":
            system_control.send_email_command(audio_text)
    else:
        st.warning("❌ No matching intent found!")
        voice.speak("I could not understand the command.")
        animation.jarvis_ui("idle")
