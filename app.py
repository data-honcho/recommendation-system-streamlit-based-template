import pandas as pd
import pickle
import streamlit as st

def recommend(movie):
    movie_index = movies_dataset[movies_dataset['title'] == movie].index[0] ## fectching the movie index
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True, key = lambda x:x[1])[1:10]
    
    recommended_movies = []

    for i in movie_list:
        recommended_movies.append(movies_dataset.iloc[i[0]].title)
    return recommended_movies

movie_dataset_dict = pickle.load(open('movies_dataset_dict.pkl', 'rb'))
movies_dataset = pd.DataFrame(movie_dataset_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommendation System')

option = st.selectbox('Select your Movie:', movies_dataset['title'].values)

if st.button('Recommend'):
    recommendations = recommend(option)
    for i in recommendations:
        st.write(i)