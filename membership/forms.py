from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from django_registration import validators

from . import models

User = get_user_model()


class LoginCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = models.Login
        fields = ('email', 'subscribed', 'published', 'member')


class LoginChangeForm(UserChangeForm):

    class Meta:
        model = models.Login
        fields = ('email', 'subscribed', 'published', 'member')


class RegistrationForm(UserCreationForm):

    class Meta:
        model = models.Login
        fields = ('email', )

    error_css_class = 'error'
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        email_field = User.get_email_field_name()
        self.fields[email_field].validators.append(
            validators.validate_confusables_email
        )
        self.fields[email_field].required = True
        self.fields[email_field].validators.append(
            validators.CaseInsensitiveUnique(
                User, email_field,
                validators.DUPLICATE_EMAIL
            )
        )
