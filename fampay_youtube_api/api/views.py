from rest_framework import filters
from .models import *
from .serializers import *
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class ListVideos(generics.ListAPIView):
    search_fields = ["title", "description"]
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)
    filterset_fields = ["channelTitle", "channelId"]
    queryset = Videos.objects.all()
    serializer_class = VideosSerializer
