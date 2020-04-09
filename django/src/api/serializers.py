from rest_framework import serializers
from home.models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('title', 'tags', 'videofile', 'longitude', 'latitude', 'author', 'pk')
