from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'country', 'phone', 'avatar')


class UserPassRecoveryForm(PasswordResetForm):

    class Meta:
        model = User
        fields = ['email']
