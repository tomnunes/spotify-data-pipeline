import boto3
import os
from datetime import date

BUCKET_NAME = "spotify-data-thomas"
today = date.today().isoformat()
LOCAL_FILE = f"data/raw/{today}/top_artists.csv"
S3_KEY = f"raw/{today}/top_artists.csv"

def upload_to_s3():
    s3 = boto3.client("s3")

    if not os.path.exists(LOCAL_FILE):
        print(f"Arquivo {LOCAL_FILE} não encontrado.")
        return
    
    try:
        s3.upload_file(LOCAL_FILE, BUCKET_NAME, S3_KEY)
        print(f"Upload realizado com sucesso para s3://{BUCKET_NAME}/{S3_KEY}")
    except Exception as e:
        print(f"Falha no upload: {e}")

if __name__ == "__main__":
    upload_to_s3()
