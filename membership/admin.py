from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import WebsiteLoginCreationForm, WebsiteLoginChangeForm
from .models import Member, WebsiteLogin


class WebsiteLoginAdmin(UserAdmin):
    add_form = WebsiteLoginCreationForm
    form = WebsiteLoginChangeForm
    model = WebsiteLogin
    list_display = ['email', 'username']


class WebsiteLoginInline(admin.StackedInline):
    model = WebsiteLogin
    exclude = ['first_name', 'last_name', 'email', 'is_staff', 'date_joined', 'is_superuser', 'user_permissions',
               'groups', 'last_login']
    fields = ['username', 'password', 'is_active']


class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Information', {'fields': [('first_name', 'middle_name', 'last_name', 'nickname'), 'date_of_birth']}),
        ('Family', {'fields': ['children']})
    ]
    list_display = ['full_name', 'age']
    exclude = []
    inlines = [WebsiteLoginInline]


admin.site.register(WebsiteLogin, WebsiteLoginAdmin)
admin.site.register(Member, MemberAdmin)
