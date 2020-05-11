from PIL import Image
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from home.models import Video
from django_countries.fields import CountryField
from home.models import skins_available


class VideoForm(forms.ModelForm):
    title = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Title'}))
    tags = forms.CharField(required=False, label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Tags'}))
    videofile = forms.FileField(required=True, label="", widget=forms.FileInput(attrs={'id': 'videofileinput', 'class': 'file-upload', 'type': 'file'}))
    #country_of_upload = forms.TypedChoiceField(coerce=str, empty_value=None, required=True, widget=forms.Select(attrs={'class': 'custom-select'}))
    country_of_upload = CountryField(blank=False, blank_label='(Select country)',).formfield( required=True, widget=forms.Select(attrs={'class': 'custom-select'}))
    video_skin = forms.ChoiceField(choices=skins_available, required=True, widget=forms.Select(attrs={'class': 'custom-select'}))
    longitude = forms.CharField(max_length=100, label="", required=True, widget=forms.TextInput(attrs={'id': 'longitudeInput', 'type': 'hidden'}))
    latitude = forms.CharField(max_length=100, label="", required=True, widget=forms.TextInput(attrs={'id': 'latitudeInput', 'type': 'hidden'}))
    
    class Meta:
        model= Video
        fields= ["title", "videofile", "tags", "country_of_upload", "video_skin", "longitude", "latitude"]
