from django_cron import CronJobBase, Schedule

# Google API
from googleapiclient.discovery import build
import apiclient
from .models import *
from fampay_youtube_api import settings
from datetime import datetime, timedelta

class FetchVideos(CronJobBase):
    RUN_EVERY_MINS = 0.1 # every 2 hour

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'api.fetch_videos'    # a unique code

    def do(self):
        pass