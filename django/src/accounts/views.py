from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.admin.models import ADDITION, LogEntry
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from accounts.forms import SignupForm, ProfileForm
from accounts.models import UserProfile
from home.models import Video
from accounts.models import Account


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/map')
    else:
        form = SignupForm()

    args = {'form': form}
    return render(request, 'accounts/signup.html', args)


def profile(request, pk=None):
    user_videos = Video.objects.filter(author=request.user)
    args = {'user_videos': user_videos, 'status': 'other'}
    return render(request, 'accounts/profile.html', args)


def profile2(request, pk=None):
    if pk:
        user = Account.objects.get(pk=pk)
        print("Other user")
    else:
        user = request.user
        print("Self")

    individual_videos = Video.objects.filter(author=user).order_by('-date_of_upload')
    args            = {'user': user, 'videos': individual_videos}
    return render(request, 'accounts/profile.html', args)


def profile_updater2(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profileForm = UserProfile.objects.get(user=request.user)
            profileForm.update(display_name=profileForm.cleaned_data['display_name'])
            profileForm.update(bio=profileForm.cleaned_data['bio'])
            profileForm.update(image=profileForm.cleaned_data['image'])
            profileForm = UserProfile()
            return HttpResponseRedirect('/')
    else:
        form = ProfileForm()

    args = {'form': form}
    return render(request, 'accounts/profile_updater.html', args)


def profile_updater(request):
    obj= get_object_or_404(UserProfile, user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance= obj)
    context= {'form': form}
    if form.is_valid():
        obj= form.save(commit= False)
        obj.save()
        messages.success(request, "You successfully updated the post")
        context= {'form': form}
        return render(request, 'accounts/profile_updater.html', context)

    else:
        context= {'form': form, 'error': 'The form was not updated successfully. Please enter in a title and content'}
        return render(request,'accounts/profile_updater.html' , context)