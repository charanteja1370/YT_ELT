import requests
import json
import os 
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env")
API_KEY = os.getenv("API_KEY")
CHANNEL_HANDLE = 'MrBeast'
maxResults = 50

def get_playlist_id():

    try: 
        url = f"https://youtube.googleapis.com/youtube/v3/channels?part=contentDetails&forHandle={CHANNEL_HANDLE}&key={API_KEY}"
        response = requests.get(url)
        # print(response)
        response.raise_for_status()

        data = response.json()

        # print(json.dumps(data, indent=4))
        # data.items[0].contentDetails.relatedPlaylists.uploads
        # data["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

        channel_items = data["items"][0]

        channel_playlistId = channel_items["contentDetails"]["relatedPlaylists"]["uploads"]

        print(channel_playlistId)
        return channel_playlistId
    except requests.exceptions.RequestException as e:
        raise e
    
 

def get_video_ids(playlistID):
    video_ids = []
    pageToken = None
    base_url = f"https://youtube.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults={maxResults}&playlistId={playlistId}&key={API_KEY}"

    try:
        while True:
            url = base_url
            if pageToken:
                url += f"&pageToken={pageToken}"
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            
            # for item in data.get("items", []): # if "items" key is missing, it will return an empty list instead of raising an error

            for item in data["items"]:
                video_ids.append(item["contentDetails"]["videoId"])

            pageToken = data.get("nextPageToken")
            if not pageToken:
                break

        return video_ids
    except requests.exceptions.RequestException as e:
        raise e


if __name__ == "__main__":
    playlistId = get_playlist_id()
    print(get_video_ids(playlistId))
else:
    print("get_playlist_id won't be executed")
