import pickle
import streamlit as st
import requests
dataset =  st.container() 
st.markdown(
    """
    <style>
    .main {
        background-color: #F5F5F5;
        }
        </style>
        """,unsafe_allow_html=True
)

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters

st.markdown("<h1 style='text-align: center; color: black;'>Movie Recommender Web App</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: black;'>Find a similar movie from a dataset of 5,000 movies!</h4>", unsafe_allow_html=True)
st.write("I found this dataset on this [Kaggle link](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata) ")

movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie you like :",
    movie_list
)
col1, col2, col3 = st.beta_columns(3)
if col2.button('Show Recommendation'):
    st.write("Recommended Movies based on your interests are :")
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])

st.title(" ")
col11, col22, col33 = st.beta_columns(3)
with col11 :
    st.markdown("<h6 style='text-align: center; color: black;'>Created by : <br> Ayman Moumen <br>  & Marwane Limouri </br>  </h6>", unsafe_allow_html=True)

with col33 :
    st.markdown("<h6 style='text-align: center; color: black;'>Supervised by : <br>M. Cédric Stéphane KOUMETIO TEKOUABOU</h6>", unsafe_allow_html=True)

