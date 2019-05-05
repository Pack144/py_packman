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
    fieldsets = [
        ('Personal Information', {'fields': [('first_name', 'middle_name', 'last_name', 'nickname'), 'date_of_birth']}),
        ('Login', {'fields': ['login']}),
        ('Family', {'fields': ['children']})
    ]
    list_display = ['full_name', 'age']
    exclude = []
    inlines = []


admin.site.register(WebsiteLogin, WebsiteLoginAdmin)
admin.site.register(Member, MemberAdmin)
