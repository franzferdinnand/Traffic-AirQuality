import os
import requests
import pandas as pd

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


# if __name__ == '__main__':
#     path_to_file = os.getenv("PATH_TO_CSV")
#     data_to_save = gather_data()
#     save_data_to_dataframe(data_to_save, path_to_file)
#     save_to_postgres(path_to_file)
