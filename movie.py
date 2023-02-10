import pandas as pd
import numpy as np
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[9].id)
engine.setProperty("rate", 175)


def Speak(audio):
    engine.say(audio)
    engine.runAndWait()




movies = pd.read_csv("movies.csv")
credits = pd.read_csv("credits.csv")

movies = movies.merge(credits, on='title')
movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
import ast


def convert(text):
    L = []
    for i in ast.literal_eval(text):
        L.append(i['name'])
    return L


movies.dropna(inplace=True)
movies['genres'] = movies['genres'].apply(convert)
movies['keywords'] = movies['keywords'].apply(convert)
import ast

ast.literal_eval(
    '[{"id": 28, "name": "Action"}, {"id": 12, "name": "Adventure"}, {"id": 14, "name": "Fantasy"}, {"id": 878, "name": "Science Fiction"}]')


def convert3(text):
    L = []
    counter = 0
    for i in ast.literal_eval(text):
        if counter < 3:
            L.append(i['name'])
        counter += 1
    return L


movies['cast'] = movies['cast'].apply(convert)
movies.head()
movies['cast'] = movies['cast'].apply(lambda x: x[0:3])


def fetch_director(text):
    L = []
    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
    return L


movies['crew'] = movies['crew'].apply(fetch_director)


def collapse(L):
    L1 = []
    for i in L:
        L1.append(i.replace(" ", ""))
    return L1


movies['cast'] = movies['cast'].apply(collapse)
movies['crew'] = movies['crew'].apply(collapse)
movies['genres'] = movies['genres'].apply(collapse)
movies['keywords'] = movies['keywords'].apply(collapse)
movies['overview'] = movies['overview'].apply(lambda x: x.split())
movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']
new = movies.drop(columns=['overview', 'genres', 'keywords', 'cast', 'crew'])

new['tags'] = new['tags'].apply(lambda x: " ".join(x))
new.head()
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(max_features=5000, stop_words='english')
vector = cv.fit_transform(new['tags']).toarray()
from sklearn.metrics.pairwise import cosine_similarity

similarity = cosine_similarity(vector)
new[new['title'] == 'The Lego Movie'].index[0]


def recommend(movie):
    index = None
    try:
        index = new[new['title'] == movie].index[0]
    except IndexError:
        while index == None:
            Speak("Please check the movie spelling.")
            movie = input("Enter a movie:")
            try:
                index = new[new['title'] == movie].index[0]
            except IndexError:
                pass

    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    Speak("Here are the recommended movies:")
    for i in distances[1:6]:
        print(new.iloc[i[0]].title)
        Speak(new.iloc[i[0]].title)
    Speak("These were the recommendations")


Speak("Please enter a movie name")
recommend(input("Enter a movie:"))

while True:
    Speak("Would you like me to recommend you another movie?")
    response = input("Would you like me to recommend you another movie? (yes/no):").lower()
    if response == 'yes':
        Speak("Please enter a movie name:")
        recommend(input("Enter a movie:"))
    else:
        break

Speak("Thank you, have a great day!")
