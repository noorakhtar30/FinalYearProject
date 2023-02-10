# libraries
import pyttsx3
import speech_recognition as sr
import datetime
import os
import pyautogui

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[9].id)
engine.setProperty("rate", 175)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said:{query}\n")
    except Exception as e:
        print("Say that again...")
        return "None"
    return query


def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "hello jarvis" in query:
            from wish_me import wishMe

            wishMe()

            while True:
                query = takeCommand().lower()
                if "take a break jarvis" in query:
                    speak("ok sir, call me anytime you need")
                    break
                elif "exit jarvis" in query:
                    speak("ok sir, have a good day sir")
                    exit()

                elif "jarvis you there" in query:
                    speak("At your services sir!")
                elif "jarvis Stands for" in query:
                    speak("It stands for Just A Rather Very Intelligent System")
                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")
                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
                elif "calculate" in query:
                    pass


                # Application
                elif "open" in query:
                    from application import openApplication
                    openApplication(query)
                elif "close" in query:
                    from application import closeApplication
                    closeApplication(query)
                elif "google" in query:
                    from search import googleSearch
                    googleSearch(query)
                elif "youtube" in query:
                    from search import youtubeSearch
                    youtubeSearch(query)
                elif "wikipedia" in query:
                    from search import wikipediaSearch
                    wikipediaSearch(query)
                elif "today's temperature" in query:
                    from search import temperature
                    temperature(query)
                elif "today's news" in query:
                    from news import latestnews
                    latestnews()
                elif "recommend" in query:
                    speak("Hold a moment sir")
                    from movie import recommend
                    recommend(query)





