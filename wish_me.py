import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[9].id)
engine.setProperty("rate", 175)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning,sir")
    elif hour > 12 and hour < 18:
        speak("Good Afternoon,sir")
    else:
        speak("Good Evening,sir")

    speak("Please tell me, how may I help you,sir")
