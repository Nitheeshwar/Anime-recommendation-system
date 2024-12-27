import requests
import json


base_url = "https://api.myanimelist.net/v2/users/@me/animelist?fields=list_status&sort=list_score"

token_file = 'D:/Nitty/Personal Projects/Anime-recommendation-system/API/key.json'
output_file = 'D:/Nitty/Personal Projects/Anime-recommendation-system/API/MAL_user_data.json'

with open(token_file) as f:
    data = json.load(f)
ACCESS_TOKEN = data['access_token']


headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}
all_anime_data = []
url = base_url

try:
    while url:  
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            json_response = response.json()
            all_anime_data.extend(json_response.get("data", []))
            url = json_response.get("paging", {}).get("next")
            print("Fetched a page of data...")
        else:
            print(f"Error {response.status_code}: {response.text}")
            break  
    
    with open(output_file, 'w') as f:
        json.dump(all_anime_data, f, indent=4)

    print("All data fetched and saved successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
