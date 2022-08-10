from django.urls import path
from .views import *

urlpatterns = [
    path("", ListVideos.as_view()),
]