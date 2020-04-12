from rest_framework import serializers
from home.models import Video
from accounts.models import Account


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('title', 'tags', 'videofile', 'longitude', 'latitude', 'author')
    
    '''def save(self):
        video = Video(
            title       = self.validated_data['title'],
            tags    = self.validated_data['tags'],
            videofile = self.validated_data['videofile'],
            longitude = self.validated_data['longitude'],
            latitude = self.validated_data['latitude'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password2': 'Passwords must match'})
        account.set_password(password)
        account.save()
        return account'''
        


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model = Account
        fields = ('username', 'email', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            email       = self.validated_data['email'],
            username    = self.validated_data['username'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password2': 'Passwords must match'})
        account.set_password(password)
        account.save()
        return account