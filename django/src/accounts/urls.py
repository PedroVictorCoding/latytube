from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from accounts.views import signup

urlpatterns = [
    path('login/', LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('signup/', signup, name="signup"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
