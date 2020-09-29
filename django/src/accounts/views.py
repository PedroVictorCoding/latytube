from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_text
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
from django.db import IntegrityError
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from .tokens import account_activation_token
from django.template.loader import render_to_string
from src.settings import EMAIL_HOST_USER
 

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.email = form.cleaned_data.get('email')
            # user can't login until link confirmed
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Please Activate Your Account'
            # load a template like get_template() 
            # and calls its render() method immediately.
            message = render_to_string('accounts/activation_request.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                # method will generate a hash value with user related data
                'token': account_activation_token.make_token(user),
            })
            # html_message = render_to_string('accounts/activation_request_html.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     # method will generate a hash value with user related data
            #     'token': account_activation_token.make_token(user),
            # })
            send_mail(
                subject,
                message,
                'latytube@gmail.com',
                [user.email,],
                )
            return HttpResponseRedirect('/sent')
    else:
        form = SignupForm()

    args = {'form': form}
    return render(request, 'accounts/signup.html', args)

def activation_sent_view(request):
    return render(request, 'accounts/activation_sent.html')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
    # checking if the user exists, if the token is valid.
    if user is not None and account_activation_token.check_token(user, token):
        # if valid set active true 
        user.is_active = True
        # set signup_confirmation true
        user.signup_confirmation = True
        user.save()
        login(request, user)
        return HttpResponseRedirect('/map')
    else:
        return render(request, 'accounts/activation_invalid.html')


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


