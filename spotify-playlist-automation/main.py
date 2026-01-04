import requests
from bs4 import BeautifulSoup
import spotipy
from dotenv import load_dotenv
import os
import pprint

load_dotenv()
from spotipy.oauth2 import SpotifyOAuth


travel_year = input("Which Year do you want to travel? Type the date in this format YYYY-MM-DD: ")
header =  {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"}

song_response = requests.get(f"https://www.billboard.com/charts/hot-100/{travel_year}/",headers=header)
print(song_response.status_code)

soup = BeautifulSoup(song_response.content, "html.parser")
top_100_songs_tag = soup.select(".o-chart-results-list-row h3#title-of-a-story")


top_100_songs = [" ".join(song.get_text().split()) for song in top_100_songs_tag]
# print(top_100_songs)


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
                        client_id=os.getenv("CLIENT_ID"),
                        client_secret=os.getenv("CLIENT_SECRET"),
                        redirect_uri=os.getenv("REDIRECT_URI"),
                        scope='playlist-modify-private'
                     ))

user_profile = sp.current_user()
user_id = user_profile['id']
# print('Current User ID:', user_id)

def get_song_uri(song_name):
    results = sp.search(q=song_name, type='track', limit=1)
    tracks = results['tracks']['items']
    if tracks:
        return tracks[0]['uri']
    else:
        return None

song_uris =[]
for song in top_100_songs:
    uri = get_song_uri(song)
    if uri:
        song_uris.append(uri)
    else:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# pprint.pp(song_uris)

playlist_data = sp.user_playlist_create(user= user_id,name=f"{travel_year} Billboard 100" ,public=False)
playlist_id = playlist_data['id']

playlist_data = sp.playlist_add_items(playlist_id, song_uris)
pprint.pp(playlist_data)