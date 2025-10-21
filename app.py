import pickle
import streamlit as st
import requests


# Helper Function(fetch image)
def fetch_poster(movie_id):
    """Fetch movie poster from TMDB API."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"
    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyMWMxMzE3YzRjZDcxOGYxMDMzZWY2MmUxYTQ2ZDM1MiIsIm5iZiI6MTc2MTA1MjU4MC45NjUsInN1YiI6IjY4Zjc4N2E0MWFkODRiNTBlZTMyMTg3YyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-AO64M_I2yOs2K00F8NrkY9F4tOTfhIB17d-GszcC6A"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    poster_path = data.get("poster_path")
    if poster_path:
        return f"https://image.tmdb.org/t/p/w500{poster_path}"
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"



#  Recommendation Logic
def recommend(movie_title):
    """Recommend similar movies based on similarity matrix."""
    if movie_title not in movies["title"].values:
        st.error(" Movie not found in database.")
        return [], []

    index = movies[movies["title"] == movie_title].index[0]
    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_titles = []
    recommended_posters = []

    for i in distances[1:6]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_titles.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_titles, recommended_posters


#  Streamlit UI

st.set_page_config(page_title=" Movie Recommender", layout="wide")
st.title(" Movie Recommendation System using ML")

# Load Data
movies = pickle.load(open('artificats/movie_list.pkl','rb'))
similarity = pickle.load(open('artificats/similary.pkl','rb'))

# Select Movie
movie_list = movies["title"].values
selected_movie = st.selectbox(" Type or select a movie to get recommendations", movie_list)

# Show Recommendations
if st.button("Show Recommended Movies"):
    recommended_titles, recommended_posters = recommend(selected_movie)

    if recommended_titles:
        cols = st.columns(5)
        for col, title, poster in zip(cols, recommended_titles, recommended_posters):
            with col:
                st.text(title)
                st.image(poster)
