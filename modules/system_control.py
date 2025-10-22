import subprocess
import platform
import webbrowser

def open_application(command_text):
    system = platform.system()
    command_text = command_text.lower()

    try:
        # Windows
        if system == "Windows":
            if "calculator" in command_text:
                subprocess.Popen("calc.exe")
            elif "notepad" in command_text:
                subprocess.Popen("notepad.exe")
            elif "paint" in command_text:
                subprocess.Popen("mspaint.exe")
            elif "word" in command_text:
                subprocess.Popen(["start", "winword"], shell=True)
            elif "excel" in command_text:
                subprocess.Popen(["start", "excel"], shell=True)
            elif "powerpoint" in command_text:
                subprocess.Popen(["start", "powerpnt"], shell=True)
            elif "browser" in command_text:
                webbrowser.open("https://www.google.com")
            else:
                print("App not configured.")

        # Mac
        elif system == "Darwin":
            if "calculator" in command_text:
                subprocess.Popen(["open", "-a", "Calculator"])
            elif "textedit" in command_text:
                subprocess.Popen(["open", "-a", "TextEdit"])
            elif "browser" in command_text:
                webbrowser.open("https://www.google.com")

        # Linux
        elif system == "Linux":
            if "calculator" in command_text:
                subprocess.Popen(["gnome-calculator"])
            elif "gedit" in command_text:
                subprocess.Popen(["gedit"])
            elif "browser" in command_text:
                webbrowser.open("https://www.google.com")

        else:
            print("Unsupported OS.")
    
    except Exception as e:
        print(f"Error opening app: {e}")
