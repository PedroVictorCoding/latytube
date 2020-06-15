from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Video
from .forms import VideoForm
from accounts.models import UserProfile, Account
import numpy as np
from django.contrib.auth.decorators import login_required
from friendship.models import Friend, Follow, Block
import random

def homepage(request):
    return render(request, 'home/homepage.html')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@login_required()
def map_view(request):
    userfollowers       = Follow.objects.followers(request.user)
    userfollowings      = Follow.objects.following(request.user)
    amountfollowers     = len(userfollowers)
    amountfollowing     = len(userfollowings)
    userprofile         = UserProfile.objects.get(user=request.user)
    user_videos         = Video.objects.filter(author=request.user).order_by('-date_of_upload')
    form                = VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        video_upload            = form.save(commit=False)
        title                   = form.cleaned_data['title']
        tags                    = form.cleaned_data['tags']
        video_upload.author     = request.user
        video_upload.like_count = 0
        video_upload.view_count = 0
        form.save()
        form                    = VideoForm()
        return HttpResponseRedirect('/map/')
        
    args = {
        'form': form, 
        'videos': user_videos,
        'amountfollowers': amountfollowers,
        'amountfollowing': amountfollowing,
        'userfollowers': userfollowers,
        'userfollowings': userfollowings,
        'userprofile': userprofile,
        # send random mapbox tile from multiple accounts to bypass pricing
        }
    return render(request, 'home/map_view.html', args)


def showvideo(request):
    lastvideos = Video.objects.all().order_by('-date_of_upload')

    form= VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        video_upload = form.save(commit=False)
        title = form.cleaned_data['title']
        tags = form.cleaned_data['tags']
        video_upload.author = request.user
        video_upload.like_count = 0
        video_upload.view_count = 0
        #video_upload.location = LonlatIPVal
        # TODO: Generate JSON inside media folder
        form.save()
    
    args= {
        'lastvideos': lastvideos,
        'form': form
              }

    return render(request, 'home/feed.html', args)


def showfullvideo(request, pk=None):
    lastvideo = Video.objects.get(id=pk)
    args = {'lastvideo': lastvideo}
    return render(request, 'home/fullvideo.html', args)
