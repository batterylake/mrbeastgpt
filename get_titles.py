import csv
import os
from googleapiclient.discovery import build
import pandas as pd

api_key = '---------------------------------------'

youtube = build('youtube', 'v3', developerKey=api_key)

def get_channel_videos(channel_id):
    res = youtube.channels().list(id=channel_id, part='contentDetails').execute()
    playlist_id = res['items'][0]['contentDetails']['relatedPlaylists']['uploads']
    print(playlist_id)
    videos = []
    next_page_token = None
    while 1:
        res = youtube.playlistItems().list(playlistId=playlist_id, part='snippet', maxResults=1000, pageToken=next_page_token).execute()
        videos += res['items']
        next_page_token = res.get('nextPageToken')
        if next_page_token is None:
            break
    return videos

mrbeast_videos = get_channel_videos("UCX6OQ3DkcsbYNE6H8uQQuVA")
file = pd.DataFrame(mrbeast_videos)
snippet = file[['snippet']]
titles = []
for i in range(len(snippet)):
    titles.append(snippet['snippet'][i]['title'])
titles = pd.DataFrame(titles)
titles.to_csv('mrbeast_videos.csv', index=False)