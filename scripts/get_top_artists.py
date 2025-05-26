import os
import json
import pandas as pd
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import spotipy
from datetime import date


load_dotenv()

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_ids = [
    '6XyY86QOPPrYVGvF9ch6wz',
    '3q7HBObVc0L8jNeTe5Gofh',
    '5JXhkyafynxCvxtov7C1PV',
    '3TVXtAsR1Inumwj472S9r4',
]

def get_artist_data(artist_id):
    data = []

    for artist_id in artist_ids:
        artist = sp.artist(artist_id)
        
        data.append({
            'id': artist['id'],
            'name': artist['name'],
            'genres': ', '.join(artist['genres']),
            'followers': artist['followers']['total'],
            'popularity': artist['popularity'],
            'timestamp': date.today().isoformat(),
            'url': artist['external_urls']['spotify']
        })

        return pd.DataFrame(data)

if __name__ == "__main__":
    df = get_artist_data(artist_ids)
    today = date.today().isoformat()
    output_path = f"data/raw/{today}/top_artists.csv"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Dados salvos em {output_path}")
