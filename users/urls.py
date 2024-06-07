from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UserConfig
from users.views import RegisterView, ProfileView, PassRecovery

app_name = UserConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('password-recovery/', PassRecovery.as_view(), name='password-recovery')
]
