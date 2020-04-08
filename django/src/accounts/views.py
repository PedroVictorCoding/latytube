from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
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


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            return HttpResponseRedirect('/')
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
        user = User.objects.get(pk=pk)
        print("Other user")
    else:
        user = request.user
        print("Self")

    individual_videos = Video.objects.filter(author=user).order_by('-date_of_upload')
    args            = {'user': user, 'videos': individual_videos}
    return render(request, 'accounts/profile.html', args)