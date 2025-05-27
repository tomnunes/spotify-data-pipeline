from prefect import flow, task
from datetime import date
from scripts.upload_to_s3 import upload_dict_as_json_to_s3

@task
def get_top_artists_data():
    # Simulação dos dados (substituir depois pelo resultado real do scraping/API)
    return [
        {"name": "Arctic Monkeys", "popularity": 85, "genres": ["indie rock"]},
        {"name": "Radiohead", "popularity": 80, "genres": ["alternative", "art rock"]},
    ]

@task
def prepare_data(artists):
    return {
        "date": date.today().isoformat(),
        "artists": artists
    }

@task
def upload_json(data):
    bucket = "spotify-data-thomas"
    key = f"processed/{data['date']}/top_artists.json"
    upload_dict_as_json_to_s3(data, bucket, key)

@flow(name="Transform and Upload JSON to S3")
def transform_and_upload_flow():
    artists = get_top_artists_data()
    data = prepare_data(artists)
    upload_json(data)

if __name__ == "__main__":
    transform_and_upload_flow()