from rest_framework import viewsets
from .serializers import VideoSerializer
from home.models import Video

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
