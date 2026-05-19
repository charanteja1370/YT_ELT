#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE airflow_metadata_db;
    CREATE DATABASE celery_results_db;
    CREATE DATABASE elt_db;

    CREATE USER airflow WITH PASSWORD 'airflow';
    GRANT ALL PRIVILEGES ON DATABASE airflow_metadata_db TO airflow;
    GRANT ALL PRIVILEGES ON DATABASE celery_results_db TO airflow;

    CREATE USER yt_api_user WITH PASSWORD 'X57tmQ846GYP3Jgb';
    GRANT ALL PRIVILEGES ON DATABASE elt_db TO yt_api_user;
EOSQL
