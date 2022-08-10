from django_cron import CronJobBase, Schedule

# Google API
from googleapiclient.discovery import build
import apiclient

from .serializers import VideosSerializer
from .models import *
from fampay_youtube_api import settings
from datetime import datetime, timedelta

class FetchVideos(CronJobBase):
    RUN_EVERY_MINS = 0.1 # every 2 hour

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'api.fetch_videos'    # a unique code


    def do(self):
        apiKeys = settings.GOOGLE_API_KEYS
        time_now = datetime.now()
        last_request_time = time_now - timedelta(minutes=5)
        res = {}
        for apiKey in apiKeys:
            if len(res)!=0:break
            try:
                youtube = build("youtube", "v3", developerKey=apiKey)
                request = youtube.search().list(q="football",part="snippet",order="date",maxResults=25,publishedAfter=(last_request_time.replace(microsecond=0).isoformat() + "Z"))
                res = request.execute()
            except apiclient.errors.HttpError as err:
                code = err.resp.status
                if not (code == 400 or code == 403):
                    print("Status Code: ",code)
                    break
        

        #Storing the data in DB
        for object in res["items"]:
            data = object["snippet"]
            serializer = VideosSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
            else:
                print(serializer.errors)