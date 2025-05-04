import os
import requests
import pandas as pd

from dotenv import load_dotenv

load_dotenv()


def gather_data():
    url = "https://api.openaq.org/v3/locations/616"
    header = {
        "Accept": "application/json",
        "X-API-Key": os.getenv('OPENAQ_API_KEY')
    }
    data = requests.get(url=url, headers=header)

    return data


def save_data_to_dataframe(data):
    data = data.json()
    data = data.get("results")
    df = pd.DataFrame(data=data)
    df.to_csv("openaq_data.csv", index=False)


if __name__ == '__main__':
    data_to_save = gather_data()
    save_data_to_dataframe(data_to_save)