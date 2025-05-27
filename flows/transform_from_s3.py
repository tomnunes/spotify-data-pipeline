from prefect import flow, task
import boto3
import pandas as pd
from io import StringIO
from datetime import date
from typing import Optional

BUCKET_NAME = "spotify-data-thomas"

@task
def read_csv_from_s3(date_str: str):
    s3 = boto3.client("s3")
    key = f"raw/{date_str}/top_artists.csv"
    response = s3.get_object(Bucket=BUCKET_NAME, Key=key)
    content = response["Body"].read().decode("utf-8")
    df = pd.read_csv(StringIO(content))
    return df

@task
def transform_data(df):
    df_transformed = df[["name", "popularity", "genres"]].copy()
    df_transformed["popularity"] = df_transformed["popularity"] / 100  # Normaliza
    return df_transformed.to_dict(orient="records")

@task
def save_transformed_to_s3(data, date_str: str):
    s3 = boto3.client("s3")
    key = f"processed/{date_str}/top_artists.json"
    content = StringIO()
    pd.DataFrame(data).to_json(content, orient="records", indent=2)
    content.seek(0)
    s3.put_object(Bucket=BUCKET_NAME, Key=key, Body=content.read())
    print(f"Arquivo salvo em: s3://{BUCKET_NAME}/{key}")

@flow(name="transform_from_S3")
def transform_from_s3_flow(date_str: Optional[str] = None):
    if not date_str:
        date_str = date.today().isoformat()
    
    df = read_csv_from_s3(date_str)
    transformed = transform_data(df)
    save_transformed_to_s3(transformed, date_str)

if __name__ == "__main__":
    transform_from_s3_flow()