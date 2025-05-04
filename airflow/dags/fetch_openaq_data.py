import os

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
sys.path.append("/opt/airflow/src")
from data_gathering import gather_data, save_data_to_dataframe, save_to_postgres


def gather_data_wrapper(**context):
    data = gather_data()
    path = os.getenv("PATH_TO_CSV")
    return save_data_to_dataframe(data, path)


def save_data_to_postgres_wrapper(**context):
    path = os.getenv("PATH_TO_CSV")
    return save_to_postgres(path)


with DAG(
    dag_id="fetch_openaq_data",
    start_date=datetime(2025,5,4),
    schedule_interval="@daily",
    catchup=False,
    tags=["openaq"],

) as dag:

    task1 = PythonOperator(python_callable=gather_data_wrapper, task_id="data_save", provide_context=True)
    task2 = PythonOperator(python_callable=save_data_to_postgres_wrapper, task_id="data_to_postgres", provide_context=True)

    task1 >> task2
