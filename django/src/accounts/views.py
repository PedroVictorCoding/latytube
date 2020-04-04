from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.contrib.admin.models import ADDITION, LogEntry
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from accounts.forms import SignupForm, ProfileForm
from accounts.models import UserProfile


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
