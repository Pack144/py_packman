from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import WebsiteLoginCreationForm, WebsiteLoginChangeForm
from .models import Member, Family, WebsiteLogin


class WebsiteLoginAdmin(UserAdmin):
    add_form = WebsiteLoginCreationForm
    form = WebsiteLoginChangeForm
    model = WebsiteLogin
    list_display = ['email', 'username']


class MemberAdmin(admin.ModelAdmin):
    model = Member
    list_display = ['first_name', 'nickname', 'last_name', 'email']


class FamilyAdmin(admin.ModelAdmin):
    list_display = ['family_name']
    search_fields = ['family_name']


admin.site.register(WebsiteLogin, WebsiteLoginAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Family, FamilyAdmin)
