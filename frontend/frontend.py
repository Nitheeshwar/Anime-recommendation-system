import streamlit as st
import requests
import pandas as pd
import genre

API_BASE_URL = "http://127.0.0.1:8000"

st.title("Anime Recommendation System")


menu = ["Genre", "MAL Username", "Anime Name"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "MAL Username":
    st.subheader("Search by MAL Username")
    mal_username = st.text_input("Enter MyAnimeList Username:")
    genre_filter = st.multiselect("Filter by Genre (optional):", genre.genrelis)
    
    if st.button("Get Recommendations"):
        payload = {"username": mal_username, "genre_filters": genre_filter}
        response = requests.post(f"{API_BASE_URL}/recommend/by-mal-username", json=payload)
        
        if response.status_code == 200:
            recommendations = response.json()
            st.success("Recommendations fetched successfully!")
            st.write(pd.DataFrame(recommendations))
        else:
            st.error(f"Error: {response.json().get('detail', 'Unknown error')}")

elif choice == "Anime Name":
    st.subheader("Search by Anime Name")
    anime_name = st.text_input("Enter Anime Name:")
    genre_filter = st.multiselect("Filter by Genre (optional):", genre.genrelis)
    
    if st.button("Get Recommendations"):
        payload = {"anime_name": anime_name, "genre_filters": genre_filter}
        response = requests.post(f"{API_BASE_URL}/recommend/by-anime-name", json=payload)
        
        if response.status_code == 200:
            recommendations = response.json()
            st.success("Recommendations fetched successfully!")
            st.write(pd.DataFrame(recommendations))
        else:
            st.error(f"Error: {response.json().get('detail', 'Unknown error')}")

elif choice == "Genre":
    st.subheader("Genre Alone")
    genre_filter = st.multiselect("Filter by Genre:", genre.genrelis)
    
    if st.button("Get Recommendations"):
        payload = {"genre_filters": genre_filter}
        response = requests.post(f"{API_BASE_URL}/recommend/by-genre", json=payload)
        
        if response.status_code == 200:
            recommendations = response.json()
            st.success("Recommendations fetched successfully!")
            st.write(pd.DataFrame(recommendations))
        else:
            st.error(f"Error: {response.json().get('detail', 'Unknown error')}")
