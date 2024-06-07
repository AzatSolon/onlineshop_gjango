from django.contrib.auth.views import LoginView
from django.urls import path

from users.apps import UserConfig
from users.views import RegisterView, ProfileView

app_name = UserConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('login/', LoginView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile', ProfileView.as_view(), name='profile'),
]
