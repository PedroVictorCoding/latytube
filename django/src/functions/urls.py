from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from .views import delete_video, search_videos, random_video, search_user, followRequest, video_in_boundary


urlpatterns = [
    # These urls should be pingged on button click
    path('delete/v/<int:video_id>', delete_video, name="delete_video"),
    path('search/v/', search_videos, name="Search Videos"),
    path('search/u/', search_user, name="Search Users"),
    path('random/v/', random_video, name="Random Video"),
    path('follow/f/<str:fromUser>/t/<str:toUser>/', followRequest, name="Follow Request"),
    path('add/v/boundary', video_in_boundary, name="Add Videos in Boundary"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
