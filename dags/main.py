from airflow import DAG
import pendulum
from datetime import timedelta, datetime
from api.video_stats import get_playlist_id, get_video_ids, batch_list, extract_video_data, save_to_json

# Define the local timezone
local_tz = pendulum.timezone("Asia/Kolkata")

# Default Args
default_args = {
    "owner": "dataengineers",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "email": "data@engineers.com",
    # 'retries': 1,
    # 'retry_delay': timedelta(minutes=5),
    "max_active_runs": 1,
    "dagrun_timeout": timedelta(hours=1),
    "start_date": datetime(2025, 1, 1, tzinfo=local_tz),
    # 'end_date': datetime(2030, 12, 31, tzinfo=local_tz),
}

with DAG(
    dag_id='produce_json',
    default_args=default_args,
    description='A DAG to produce JSON file with raw data',
    schedule='0 14 * * *',  # At 14:00 (2 PM) every day
    catchup=False,
) as dag:
    #Define the tasks
    playlistId = get_playlist_id()
    video_ids = get_video_ids(playlistId)
    extract_data = extract_video_data(video_ids=video_ids)
    save_to_json_task = save_to_json(extacted_data=extract_data)

    #Define the task dependencies
    playlistId >> video_ids >> extract_data >> save_to_json_task

# from airflow.decorators import dag, task
# from datetime import datetime
# import pendulum

# from api.video_stats import (
#     get_playlist_id,
#     get_video_ids,
#     extract_video_data,
#     save_to_json
# )

# local_tz = pendulum.timezone("Asia/Kolkata")


# @dag(
#     dag_id="produce_json",
#     schedule="0 14 * * *",
#     start_date=datetime(2025, 1, 1, tzinfo=local_tz),
#     catchup=False,
# )
# def produce_json():

#     @task
#     def fetch_playlist():
#         return get_playlist_id()

#     @task
#     def fetch_video_ids(playlistId):
#         return get_video_ids(playlistId)

#     @task
#     def extract_data(video_ids):
#         return extract_video_data(video_ids)

#     @task
#     def save_json(data):
#         save_to_json(data)

#     playlist = fetch_playlist()
#     video_ids = fetch_video_ids(playlist)
#     extracted = extract_data(video_ids)
#     save_json(extracted)

# dag = produce_json()