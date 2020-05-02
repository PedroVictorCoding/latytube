from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import VideoViewSet, registration_view, LogoutUserAPIView

router = routers.DefaultRouter()
router.register('videos', VideoViewSet, 'videos')

app_name = 'account'

urlpatterns = [
    path('', include(router.urls)),
    path('registration/', registration_view, name='registration_api'),
    path('login/', obtain_auth_token, name="login_api"),
    path('logout/', LogoutUserAPIView.as_view(), name='auth_user_logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
