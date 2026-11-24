
import streamlit as st
import pickle
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=f37c4844cc559df7081a38f2baa6c8ec&language=en-US".format(movie_id))

    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]



def recomended(movie):

    movie_index = movies_list[movies_list["title"] == movie].index[0]

    distance = similarity[movie_index]

    movies = sorted(
        list(enumerate(distance)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recomended_list = []
    recomended_movies_image = []

    for i in movies:
        movie_id = movies_list.iloc[i[0]].movie_id
        recomended_list.append(movies_list.iloc[i[0]].title)
        #api part of the code 
        recomended_movies_image.append(fetch_poster(movie_id))

    return recomended_list,recomended_movies_image


movies_list = pickle.load(open("movies_data.pkl", "rb"))

movie_titles = movies_list["title"].values

similarity = pickle.load(open("similarity.pkl", "rb"))


st.title("Movie Recommender System")

option = st.selectbox(
    "Please select the Movie",
    movie_titles
)

if st.button("Recommend"):

    name, poster = recomended(option)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.text(name[i])
            st.image(poster[i])