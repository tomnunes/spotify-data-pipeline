import os
import json
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import spotipy
from datetime import datetime

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

artist_ids = [
    '6XyY86QOPPrYVGvF9ch6wz',
    '3q7HBObVc0L8jNeTe5Gofh',
    '5JXhkyafynxCvxtov7C1PV'
]

def get_artist_data(artist_id):
    artist = sp.artist(artist_id)
    return {
        "id": artist["id"],
        "name": artist["name"],
        "genres": artist["genres"],
        "followers": artist["followers"]["total"],
        "popularity": artist["popularity"],
        "timestamp": datetime.utcnow().isoformat()
    }

data = [get_artist_data(artist_id) for artist_id in artist_ids]

df = pd.DataFrame(data)
df.to_csv("data/raw/artists.csv", index=False)

print("Dados salvos com sucesso em data/raw/artists.csv")
