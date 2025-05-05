# 🌫️ Air Quality Data Pipeline

A production-ready data pipeline that collects real-time air quality data from the OpenAQ API, stores it in a PostgreSQL database, and uploads processed CSV files to AWS S3. All processes are orchestrated with Apache Airflow running in Docker Compose.

## 🚀 Key Features

* 🔄 **Automated ETL**: Daily scheduled data ingestion via Airflow
* 🌍 **OpenAQ API**: Pulls air quality data from selected locations
* 🧪 **Data Validation & Export**: Saves data to both PostgreSQL and CSV
* ☁️ **AWS S3 Integration**: Archives daily snapshots to Amazon S3
* 🐳 **Dockerized**: Fully containerized for local or cloud deployment
* 📅 **Airflow DAG**: Orchestrates the entire flow with clear task dependencies

---

## ⚙️ Technologies Used

| Layer                  | Tools                   |
| ---------------------- |-------------------------|
| Workflow Orchestration | Apache Airflow (v2.9.1) |
| Data Source            | OpenAQ API              |
| Data Storage           | PostgreSQL              |
| Cloud Storage          | AWS S3                  |
| Containerization       | Docker + Docker Compose |
| Language               | Python 3.11             |

---

## 📁 Project Structure

```
.
├── airflow/
│   ├── dags/
│   │   └── fetch_openaq_data.py
│   └── logs/ ...
├── src/
│   └── data_gathering.py
├── .env
├── docker-compose.yml
└── requirements.txt
```

---

## 🧠 What You'll Learn

* How to build real-world ETL pipelines
* How to orchestrate workflows with Airflow
* How to interact with REST APIs
* How to store and archive data in PostgreSQL and AWS S3
* How to configure and manage Python projects in Docker

---

## 🔐 Environment Variables

Configure your `.env` file with:

```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres_password
POSTGRES_DB=air_quality

OPENAQ_API_KEY=your_openaq_api_key
PATH_TO_CSV=/opt/airflow/src/openaq_data.csv

AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
AWS_REGION=us-east-1
S3_BUCKET_NAME=air-quality-data

AIRFLOW__CORE__EXECUTOR=LocalExecutor
AIRFLOW__CORE__FERNET_KEY=random_generated_key
AIRFLOW__CORE__DAGS_ARE_PAUSED_AT_CREATION=True
AIRFLOW__CORE__LOAD_EXAMPLES=False
AIRFLOW_UID=50000
```

---

## ▶️ Usage

```bash
docker compose up --build
```

* Visit Airflow at: [http://localhost:8080](http://localhost:8080)
* Trigger the DAG named `fetch_openaq_data`
* Check your PostgreSQL DB and S3 bucket for results

---

## 📌 TODO (Next Steps)

* [ ] Support multiple cities (parallel DAGs)
* [ ] Airflow XCom/Sensors for smarter automation
* [ ] AWS Athena integration for querying S3 data
* [ ] dbt models for PostgreSQL analytics
* [ ] Slack/email monitoring notifications

---

## ✍️ Author

Created by \ Serhii Turchyn — Python Backend & Aspiring Data Engineer
