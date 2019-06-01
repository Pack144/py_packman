from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from . import models


class LoginCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = models.Login
        fields = ('email', 'subscribed', 'published', 'member')


class LoginChangeForm(UserChangeForm):

    class Meta:
        model = models.Login
        fields = ('email', 'subscribed', 'published', 'member')
