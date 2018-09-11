from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Member


class MemberCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Member
        fields = UserCreationForm.Meta.fields + ('nickname',)


class MemberChangeForm(UserChangeForm):

    class Meta:
        model = Member
        fields = '__all__'
