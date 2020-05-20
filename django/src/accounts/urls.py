from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetCompleteView
from accounts.views import signup, profile2

urlpatterns = [
    path('login/', LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('logout/', LogoutView.as_view(template_name="accounts/logout.html"), name='logout'),
    path('signup/', signup, name="signup"),
    path('profile/', profile2, name="profile"),
    path('profile/<str:pk>/', profile2, name="profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
