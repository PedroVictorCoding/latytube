from django.shortcuts import render, HttpResponseRedirect
from django.db.models import Q
from home.models import Video, VideoComments
from accounts.models import Account, UserProfile
from friendship.models import Friend, Follow, Block
from functions.models import PostVisualization, PostLike

def delete_video(request, video_id):
    video_to_delete = Video.objects.get(id=video_id)
    if request.user == video_to_delete.author:
        print("Author Detected")
        video_to_delete.delete()
    else:
        return HttpResponseRedirect('/feed')

    args = {'title': 'Video Deleted',}
    return render(request, 'functions/standard_function.html', args)


def search_videos(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''

    searchable_videos = Video.objects.filter(tags__icontains=search_text)
    args = {'search_elements': searchable_videos}
    return render(request, 'home/ajax/ajax_search.html', args)


def search_user(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''

    requestsSent = Friend.objects.sent_requests(user=request.user)
    searchable_users = Account.objects.filter(username__icontains=search_text).exclude(username=request.user.username)
    args = {'search_elements': searchable_users}
    return render(request, 'home/ajax/ajax_search_users.html', args)


def followRequest(request, fromUser, toUser):
    if request.method == "POST":
        other_user = Account.objects.get(pk=toUser)
        Friend.objects.add_friend(request.user, other_user)
    return render(request, 'base.html')


def random_video(request):
    if request.method == "POST":
        randomvideo = Video.objects.order_by('?')[:1]
    else:
        randomvideo = ''
    args = {'randomvideo': randomvideo}
    print(args)
    return render(request, 'home/individual_video.js', args)

def video_in_boundary(request):
    if request.method == "POST":
        NELat           = float(request.POST['NELat'])
        NELng           = float(request.POST['NELng'])
        SWLat           = float(request.POST['SWLat'])
        SWLng           = float(request.POST['SWLng'])
        videoQuantity   = int(request.POST['videoQuantity'])
        currentMarkers  = request.POST.getlist('currentMarkers[]')
        #newVideos = Video.objects.filter(Q(latitude >= SWLat) | Q(latitude <= NELat) & Q(longitude >= SWLng) | Q(longitude <= NELng))
        newVideos = Video.objects.exclude(id__in=currentMarkers).filter(latitude__gte = SWLat, latitude__lte = NELat, longitude__gte = SWLng, longitude__lte = NELng).order_by('?')[:videoQuantity]
        args = {'newVideos': newVideos}
    return render(request, 'home/ajax/addVideos.html', args)

def update_profile_image(request):
    if request.method == "POST":
        print("POST Request: " + str(request.POST))
        newImage = request.POST.getlist('image')
        updatingImage = UserProfile.objects.get(user=request.user)
        updatingImage.image = newImage
        updatingImage.save()
        updatedUserProfileInfo = UserProfile.objects.get(user=request.user)
        args = {'updatedUserProfileInfo': updatedUserProfileInfo}
    return render(request, 'home/ajax/profile_image_update.html', args)

def post_visualization(request, videopk):
    if request.method == 'POST':
        video_fk = Video.objects.get(pk=videopk)
        fromUser = Account.objects.get(email=request.user)
        try:
            PostVisualization.objects.get(post_id=video_fk, from_user=fromUser)
        except PostVisualization.DoesNotExist:
            new_view = PostVisualization(post_id=video_fk, from_user=fromUser)
            new_view.save()
            new_view_count = Video.objects.get(id=video_fk.id)
            new_view_count.view_count += 1
            new_view_count.save()
    return render(request, 'functions/empty.html')

def post_like(request, videopk):
    if request.method == 'POST':
        video_fk = Video.objects.get(pk=videopk)
        fromUser = Account.objects.get(email=request.user)
        try:
            PostLike.objects.get(post_id=video_fk, from_user=fromUser)
        except PostLike.DoesNotExist:
            new_like = PostLike(post_id=video_fk, from_user=fromUser)
            new_like.save()
            new_like_count = Video.objects.get(id=video_fk.id)
            new_like_count.like_count += 1
            new_like_count.save()
    return render(request, 'functions/empty.html')

def get_post_comment(request, videopk):
    if request.method == 'POST':
        video_comments = VideoComments.objects.filter(video_id=videopk)
    return render(request, 'functions/comments_box.html', {'video_comments': video_comments})


def post_comment(request, videopk):
    if request.method == 'POST':
        video_obj = Video.objects.get(id=videopk)
        add_new_comment = VideoComments(video_id=video_obj, author=request.user, message=request.POST['comments_message'])
        add_new_comment.save()
    return render(request, 'functions/empty.html')