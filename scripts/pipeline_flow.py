from prefect import flow
from datetime import date, datetime
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import boto3
from dotenv import load_dotenv

load_dotenv()

@flow(name="spotify_pipeline")
def spotify_pipeline(date_str: str):
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Formato inválido de data. Use o padrão YYYY-MM-DD.")

    print(f"✅ Parâmetro de data recebido corretamente: {date_str}")    


    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    artist_ids = [
        '6XyY86QOPPrYVGvF9ch6wz',
        '3q7HBObVc0L8jNeTe5Gofh',
        '5JXhkyafynxCvxtov7C1PV',
        '3TVXtAsR1Inumwj472S9r4',
    ]

    data = []
    for artist_id in artist_ids:
        artist = sp.artist(artist_id)
        data.append({
            'name': artist['name'],
            'popularity': artist['popularity'],
            'followers': artist['followers']['total'],
            'genres': ', '.join(artist['genres']),
            'url': artist['external_urls']['spotify']
        })

    df = pd.DataFrame(data)

    today = date.today().isoformat()
    output_path = f"data/raw/{today}/top_artists.csv"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"Arquivo salvo localmente: {output_path}")

    # Upload to S3
    s3 = boto3.client("s3")
    s3.upload_file(output_path, "spotify-data-thomas", f"raw/{today}/top_artists.csv")

    print(f"Upload realizado para s3://spotify-data-thomas/raw/{today}/top_artists.csv")
