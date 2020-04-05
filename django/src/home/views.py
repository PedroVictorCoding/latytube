from django.shortcuts import render
from .models import Video
from .forms import VideoForm

def homepage(request):
    consumer_ip = get_client_ip(request)
    print("Consumer IP: " + consumer_ip)
    return render(request, 'home/homepage.html')


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip



def map_view(request):
    return render(request, 'home/map_view.html')



def showvideo(request):

    lastvideos = Video.objects.all().order_by('-date_of_upload')

    form= VideoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        video_upload = form.save(commit=False)
        video_upload.author = request.user
        #video_upload.location = LonlatIPVal
        # TODO: Generate JSON inside media folder
        form.save()

    
    context= {
        'lastvideos': lastvideos,
        'form': form
              }
    
      
    return render(request, 'home/feed.html', context)
