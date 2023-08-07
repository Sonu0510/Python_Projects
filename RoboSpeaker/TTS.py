
import win32com.client

while True:
    text = input("Enter what to speak: ")
    if text == "q":
        speak = win32com.client.Dispatch("SAPI.SpVoice")
        speak.Speak("Bye Bye Amigo")
        break
    speak = win32com.client.Dispatch("SAPI.SpVoice")
    speak.Speak(text)





