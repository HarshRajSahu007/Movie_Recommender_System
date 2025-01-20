import streamlit as st
import pickle
import pandas as pd

# Load similarity matrix and movie list
similarity = pickle.load(open('similarity.pkl', 'rb'))
movies_df = pickle.load(open('movies.pkl', 'rb'))  # Assuming it's a DataFrame

# Extract movie titles as a list for dropdown
movies_list = movies_df['title'].values

st.title('Movie Recommender System')


def recommend(movie):
    # Find the index of the movie title
    movie_index = movies_df[movies_df['title'] == movie].index[0]

    # Get the similarity scores for that movie
    distances = similarity[movie_index]

    # Get the top 5 recommended movies (excluding the first one)
    movies_indices = sorted(enumerate(distances), key=lambda x: x[1], reverse=True)[1:6]
    recommended_movies=[]
    # Append recommended movie titles
    for i in movies_indices:
       movie_id=i[0]

       recommended_movies.append(movies_df.iloc[i[0]].title)

    return recommended_movies


# Dropdown to select a movie
option = st.selectbox(
    'Type Any Movie Name',
    movies_list
)

# Button to show recommendations
if st.button('Recommend'):
    recommendations = recommend(option)
    st.subheader('Recommended Movies:')
    for movie in recommendations:
        st.write(movie)
