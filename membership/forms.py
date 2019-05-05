from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import WebsiteLogin


class WebsiteLoginCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = WebsiteLogin
        fields = ('username', 'email')


class WebsiteLoginChangeForm(UserChangeForm):

    class Meta:
        model = WebsiteLogin
        fields = ('username', 'email')
