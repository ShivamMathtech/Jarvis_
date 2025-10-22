import streamlit as st
from modules import intents, system_control, gemini_api, voice, animation
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
# Animation Placeholder
# ---------------------------
animation_placeholder = st.empty()
waveform_placeholder = st.empty()

def update_animation(state):
    """Update Jarvis animation and waveform in placeholders."""
    animation_placeholder.empty()
    waveform_placeholder.empty()
    with animation_placeholder:
        animation.jarvis_ui(state)
    with waveform_placeholder:
        animation.live_waveform()

# ---------------------------
# Startup Greeting
# ---------------------------
update_animation("idle")
st.subheader("Hello, I am Jarvis. How can I assist you today?")
voice.speak("Hello, I am Jarvis. How can I assist you today?")

# ---------------------------
# Voice / Text Input
# ---------------------------
command_input = st.text_input("Type your command (or press Speak button)", "")

if st.button("🎙️ Speak") or command_input:
    update_animation("listening")
    audio_text = voice.listen_command(duration=5)

    # If microphone not detected, fallback to text input
    if not audio_text:
        if not command_input:
            audio_text = st.text_input("⚠️ Microphone not detected. Please type your command:", "")
        else:
            audio_text = command_input

    if audio_text:
        st.write(f"**You said:** {audio_text}")
        st.session_state["recent_commands"].append(audio_text)

        update_animation("processing")
        time.sleep(0.5)

        matched_intent = intents.match_intent(all_intents, audio_text)
        if matched_intent:
            response = matched_intent["responses"][0]
            st.success(f"**Jarvis:** {response}")
            voice.speak(response)
            update_animation("speaking")

            # Example system control hooks
            if matched_intent["tag"] == "open_app":
                system_control.open_application(audio_text)
            elif matched_intent["tag"] == "send_email":
                system_control.send_email_command(audio_text)

        else:
            st.warning("❌ No matching intent found!")
            voice.speak("I could not understand the command.")
            update_animation("idle")
