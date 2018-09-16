from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import MemberCreationForm, MemberChangeForm
from .models import Member


class MemberAdmin(UserAdmin):
    add_form = MemberCreationForm
    form = MemberChangeForm
    model = Member
    list_display = ['username', 'first_name', 'nickname', 'last_name', 'email']


admin.site.register(Member, UserAdmin)
admin.site.unregister(Group)
