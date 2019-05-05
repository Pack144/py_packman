from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import WebsiteLoginCreationForm, WebsiteLoginChangeForm
from .models import Member, WebsiteLogin


class WebsiteLoginAdmin(UserAdmin):
    add_form = WebsiteLoginCreationForm
    form = WebsiteLoginChangeForm
    model = WebsiteLogin
    list_display = ['email', 'username']


class MemberAdmin(admin.ModelAdmin):
    model = Member
    list_display = ['first_name', 'nickname', 'last_name', 'get_age']
    exclude = []
    inlines = []


admin.site.register(WebsiteLogin, WebsiteLoginAdmin)
admin.site.register(Member, MemberAdmin)
