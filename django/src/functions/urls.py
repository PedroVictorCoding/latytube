from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from .views import delete_video


urlpatterns = [
    path('delete/v/<int:video_id>', delete_video, name="delete_video"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
