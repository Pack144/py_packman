from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import MemberCreationForm, MemberChangeForm
from .models import Member, Family


class MemberAdmin(UserAdmin):
    add_form = MemberCreationForm
    form = MemberChangeForm
    model = Member
    list_display = ['username', 'first_name', 'nickname', 'last_name', 'email']


class FamilyAdmin(admin.ModelAdmin):
    list_display = ('family_name',)
    search_fields = ['family_name', ]


admin.site.register(Member, MemberAdmin)
admin.site.unregister(Group)
admin.site.register(Family, FamilyAdmin)
