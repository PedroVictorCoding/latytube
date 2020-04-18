from PIL import Image
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from home.models import Video


class VideoForm(forms.ModelForm):
    title = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}))
    tags = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Tags'}))
    videofile = forms.FileField(required=True, label="", widget=forms.FileInput(attrs={'id': 'videofileinput', 'class': 'file-upload', 'type': 'file'}))
    
    class Meta:
        model= Video
        fields= ["title", "videofile", "tags"]
