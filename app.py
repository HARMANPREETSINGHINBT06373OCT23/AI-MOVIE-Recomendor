import streamlit as st
import pandas as pd
import requests
import pickle
import time
import os
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

# Google Drive file ID and default poster
GDRIVE_FILE_ID = "1_a6Wgg211SmqK8I8doJgg21FKBhvqnWU"
DEFAULT_POSTER = "https://via.placeholder.com/300x450?text=No+Poster"
API_KEY = '7b995d3c6fd91a2284b4ad8cb390c7b8'

# Download .pkl from Google Drive if not already present
@st.cache_data(show_spinner="Loading movie data...")
def download_and_load_pickle():
    if not os.path.exists("movie_data.pkl"):
        download_url = f"https://drive.google.com/uc?export=download&id={GDRIVE_FILE_ID}"
        response = requests.get(download_url)
        with open("movie_data.pkl", "wb") as f:
            f.write(response.content)
    with open("movie_data.pkl", "rb") as file:
        return pickle.load(file)

# Load movie data
movies, cosine_sim = download_and_load_pickle()

# Setup retry-enabled requests session
def create_retry_session():
    session = requests.Session()
    retry = Retry(total=3, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    return session

session = create_retry_session()

# Fetch movie poster
@st.cache_data(show_spinner=False)
def fetch_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}'
    try:
        response = session.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        poster_path = data.get('poster_path')
        return f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else DEFAULT_POSTER
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster for movie ID {movie_id}: {e}")
        return DEFAULT_POSTER

# Get movie recommendations
def get_recommendations(title):
    try:
        idx = movies[movies['title'] == title].index[0]
    except IndexError:
        st.error("Selected movie not found in dataset.")
        return pd.DataFrame(columns=['title', 'movie_id'])

    sim_scores = sorted(list(enumerate(cosine_sim[idx])), key=lambda x: x[1], reverse=True)[1:11]
    movie_indices = [i[0] for i in sim_scores]
    return movies[['title', 'movie_id']].iloc[movie_indices]

# Streamlit UI
st.title("🎬 Movie Recommendation System")
selected_movie = st.selectbox("Select a movie:", movies['title'].values)

if st.button('Recommend'):
    recommendations = get_recommendations(selected_movie)

    if not recommendations.empty:
        st.write(f"Top 10 recommended movies for: **{selected_movie}**")
        poster_urls = []

        for i in range(0, 10, 5):
            cols = st.columns(5)
            for col, j in zip(cols, range(i, i + 5)):
                if j < len(recommendations):
                    movie_title = recommendations.iloc[j]['title']
                    movie_id = recommendations.iloc[j]['movie_id']
                    time.sleep(0.2)
                    poster_url = fetch_poster(movie_id)
                    poster_urls.append((poster_url, movie_title))

                    with col:
                        st.image(poster_url, width=130)
                        st.caption(movie_title)

        if any("via.placeholder.com" in poster_url for poster_url, _ in poster_urls):
            st.warning("⚠️ Some posters couldn't be loaded. Please check your network connection or try again later.")
