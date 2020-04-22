from django.shortcuts import render
from .models import Video
from .forms import VideoForm
import numpy as np
from pinax.points.models import points_awarded, award_points

def homepage(request):
    return render(request, 'home/homepage.html')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def map_view(request):
    map_videos = Video.objects.all()
    usertotalpoints = points_awarded(request.user)
    print(usertotalpoints)
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
        
    args = {'map_videos': map_videos, 'form': form}
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

