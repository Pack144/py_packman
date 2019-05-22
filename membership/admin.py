from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import WebsiteLoginCreationForm, WebsiteLoginChangeForm
from .models import Member, WebsiteLogin, Parent, Scout, Contributor


class WebsiteLoginAdmin(UserAdmin):
    add_form = WebsiteLoginCreationForm
    form = WebsiteLoginChangeForm
    model = WebsiteLogin
    list_display = ['email', 'username']


class WebsiteLoginInline(admin.StackedInline):
    model = WebsiteLogin
#    exclude = ['first_name', 'last_name', 'email', 'is_staff', 'date_joined', 'is_superuser', 'user_permissions',
#               'groups', 'last_login']
#    fields = ['username', 'is_active']


class MemberAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Personal Information', {'fields': [('first_name', 'middle_name', 'last_name', 'nickname'),
                                             'date_of_birth',
                                             'avatar']}),
                                ('Family', {'fields': ['children']})
    ]
    list_display = ['name', 'last_name', 'age']
    list_display_links = ['name', 'last_name']
    exclude = []
    inlines = [WebsiteLoginInline]


admin.site.register(WebsiteLogin, WebsiteLoginAdmin)
admin.site.register(Member, MemberAdmin)

admin.site.register(Contributor)
admin.site.register(Parent)
admin.site.register(Scout)
