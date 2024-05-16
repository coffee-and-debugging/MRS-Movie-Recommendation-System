import streamlit as st
import pickle
from function import recommend

st.markdown('<marquee><p style="text-align: center; font-family: Courier; color: white; font-size: 30px;">MRS: Movie Recommendation System</p></marquee>', unsafe_allow_html=True)

movies = pickle.load(open("movie_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))
movie_titles = movies['title'].values
selected_movie = st.selectbox("Select a movie:", movie_titles)
if st.button("Recommend me! "):
    rec_names, rec_posters = recommend(selected_movie, movies, similarity)
    cols = st.columns(5)
    for col, name, poster in zip(cols, rec_names, rec_posters):
        col.text(name)
        col.image(poster)
