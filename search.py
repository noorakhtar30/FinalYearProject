import webbrowser
import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import requests
from bs4 import BeautifulSoup


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source, 0, 4)
    try:
        print("Understanding...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said:{query}\n")
    except Exception as e:
        print("Say that again...")
        return "None"
    return query


query = takeCommand().lower()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[9].id)
engine.setProperty("rate", 175)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def googleSearch(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis", "")
        query = query.replace("google search", "")
        query = query.replace("google", "")
        speak("This is what I found on google")
        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query, 2)
            speak(result)
        except:
            speak("Couldn't find any information")


def youtubeSearch(query):
    if "youtube" in query:
        speak("This is what I found on google")
        query = query.replace("youtube", "")
        query = query.replace("youtube search", "")
        query = query.replace("jarvis", "")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Hope you enjoy sir")


def wikipediaSearch(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("wikipedia", "")
        query = query.replace("wikipedia search", "")
        query = query.replace("jarvis", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia..")
        print(results)
        speak(results)


def temperature(query):
    if "temperature" in query:
        search = "temperature in pune"
        url = f"https://www.google.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        speak(f"current{search} is {temp}")

