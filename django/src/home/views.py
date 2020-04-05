from django.shortcuts import render
from .models import Video
from .forms import VideoForm

def homepage(request):
    return render(request, 'home/homepage.html')

def map_view(request):
    return render(request, 'home/map_view.html')



def showvideo(request):

    lastvideos = Video.objects.all().order_by('-date_of_upload')

    form= VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        video_upload = form.save(commit=False)
        video_upload.author = request.user
        # TODO: Generate JSON inside media folder
        form.save()

    
    context= {
        'lastvideos': lastvideos,
        'form': form
              }
    
      
    return render(request, 'home/feed.html', context)
