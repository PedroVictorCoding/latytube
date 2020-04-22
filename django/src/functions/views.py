from django.shortcuts import render, HttpResponseRedirect
from home.models import Video

def delete_video(request, video_id):
    video_to_delete = Video.objects.get(id=video_id)
    if request.user == video_to_delete.author:
        print("Author Detected")
        video_to_delete.delete()
    else:
        return HttpResponseRedirect('/feed')

    args = {'title': 'Video Deleted',}
    return render(request, 'functions/standard_function.html', args)



## Achievements Functions

def share_link(request, user_id):
    pass