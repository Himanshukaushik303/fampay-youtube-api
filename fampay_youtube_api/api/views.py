from rest_framework import filters
from .models import *
from .serializers import *
from rest_framework import generics
# Create your views here.

class ListVideos(generics.ListAPIView):
    search_fields = ["title", "description"]
    filter_backends = (filters.SearchFilter,)
    filterset_fields = ["channelTitle", "channelId"]
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer
