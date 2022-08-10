from email.policy import default
from django.db import models

# Create your models here.
class Videos(models.Model):
    title = models.TextField(blank =True)
    description = models.TextField(blank =True,null=True)
    thumbnails = models.JSONField(default=dict,blank=True)
    channelId = models.CharField(max_length=256,blank=True)
    channelTitle = models.TextField(blank=True)
    publishTime = models.DateTimeField()

    class Meta:
        ordering = ['-publishTime']


