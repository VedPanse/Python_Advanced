import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth


the_time = input("Enter the year you want to travel back (YYYY-MM-DD): ")
URL = f"https://www.billboard.com/charts/hot-100/{the_time}"

CLIENT_ID = "8a47af16bf9f4c85905b8b9690145ce2"
CLIENT_SECRET = "5bd18b2169bd46e78c207e0628c442c3"

requests = requests.get(url=URL)
web_page = requests.text

soup = BeautifulSoup(web_page, "html.parser")
names = soup.find_all(name="span", class_="chart-element__information__song")

songs = [song_names.getText() for song_names in names]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)
