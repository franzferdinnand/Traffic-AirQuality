import logging
import os
from datetime import datetime

import boto3
import requests
import pandas as pd
from botocore.exceptions import ClientError

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()


def gather_data():
    url = "https://api.openaq.org/v3/locations/616"
    header = {
        "Accept": "application/json",
        "X-API-Key": os.getenv('OPENAQ_API_KEY')
    }
    data = requests.get(url=url, headers=header)

    return data


def save_data_to_dataframe(data, path_to_csv):
    data = data.json()
    data = data.get("results")
    df = pd.DataFrame(data=data)
    df.to_csv(path_to_csv, index=False)


def save_to_postgres(path):
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgres_password")
    host = os.getenv("POSTGRES_HOST", "db")
    port = os.getenv("POSTGRES_PORT", "5432")
    db = os.getenv("POSTGRES_DB", "traffic_airquality")

    df = pd.read_csv(path)

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')

    df.to_sql('air_quality', engine, if_exists='append', index=False)


def upload_to_s3(filename, object_name=None):
    if object_name is None:
        date_str = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
        base_filename = os.path.basename(filename)
        object_name = f"airflow_exports/{base_filename}_{date_str}.csv"

    bucket = os.getenv("S3_BUCKET_NAME")

    s3 = boto3.client("s3")
    try:
        s3.upload_file(filename, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


if __name__ == '__main__':
    upload_to_s3()
