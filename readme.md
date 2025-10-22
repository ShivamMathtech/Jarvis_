# 🦾 Ultimate Jarvis AI - Real Time

**Ultimate Jarvis AI** is a real-time voice and text-based assistant built with Python and Streamlit. Jarvis can respond to user commands, detect intents, and give responses in **voice format**. It also supports fallback to text input when the microphone is not available.

---

## **Features**

- 🎙️ Voice input and output (via pyttsx3)
- 📝 Text input fallback if microphone not detected
- 🤖 Animated Jarvis UI for real-time interactions
- 💡 Intent detection via `intents.json`
- 🗂️ Command history tracking
- 🖥️ System control for opening apps or performing tasks
- 🌐 Real-time web app using Streamlit

---

## **Getting Started (Local)**

### **Prerequisites**

- Python 3.10 or higher
- Install required packages:

```bash
pip install -r requirements.txt
```

## Run the App

streamlit run main.py

## Folder Structure

JarvisAI/
│
├─ main.py
├─ requirements.txt
├─ intents.json
├─ modules/
│ ├─ intents.py
│ ├─ voice.py
│ ├─ animation.py
│ └─ system_control.py
└─ README.md
