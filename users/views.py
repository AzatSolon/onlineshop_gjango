import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserProfileForm, UserPassRecoveryForm, UserRegisterForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        token = secrets.token_hex(16)
        user.token = token
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}'
        send_mail(subject='Подтверждение почты',
                  message=f'Подтвердите почту{url}',
                  from_email=EMAIL_HOST_USER,
                  recipient_list=[user.email])
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


class PassRecovery(LoginRequiredMixin, UpdateView):
    models = User
    form_class = UserPassRecoveryForm
    template_name = 'users/pass_recovery.html'
    success_url = reverse_lazy('users:login')


def email_verification(token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))


def send_message(request):
    return render(request, 'users/send_message.html')
