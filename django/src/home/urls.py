from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from home.views import homepage, map_view, showvideo, showfullvideo

urlpatterns = [
    path('', homepage, name='homepage'),
    path('map/', map_view, name='map'),
    path('feed/', showvideo, name="feed"),
    path('feed/v/<int:pk>', showfullvideo, name="individualvid")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
