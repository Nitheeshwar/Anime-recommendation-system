import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import json


token_file = 'D:/Nitty/Personal Projects/Anime-recommendation-system/API/key.json'
with open(token_file) as f:
    data = json.load(f)
ACCESS_TOKEN = data['access_token']

def fetch_anime_data(anime_id,anime_df):
    url = f"https://api.myanimelist.net/v2/anime/{anime_id}?fields=genres,main_picture,title,title_english,title_japanese,rating"
    headers = {"Authorization": f"Bearer {ACCESS_TOKEN}"}
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            
            genre = ", ".join([g['name'] for g in data.get('genres', [])])
            image_url = data.get('main_picture', {}).get('large', None)
            
            print(f"anime {anime_id}:{genre}, {image_url}")
            return genre, image_url
        
    except Exception as e:
        print(f"Error fetching data for anime_id {anime_id}: {e}")
    return None, None, None, None, None



anime_df = pd.read_csv("D:/Nitty/Personal Projects/Anime-recommendation-system/anime_dataset/anime_cleaned.csv")

for index, row in anime_df.iterrows():
    if any(pd.isna(row[col]) for col in ['genre', 'image_url']):
        genre, image_url= fetch_anime_data(row['anime_id'],anime_df)
        
        if pd.isna(row['genre']):
            anime_df.at[index, 'genre'] = genre
        if pd.isna(row['image_url']):
            anime_df.at[index, 'image_url'] = image_url


anime_df.to_csv("D:/Nitty/Personal Projects/Anime-recommendation-system/anime_dataset/Anime_Final.csv", index=False)

