from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import WebsiteLoginCreationForm, WebsiteLoginChangeForm
from .models import Member, WebsiteLogin, Parent, Scout, Contributor
from assignments.models import Committee, Den


class WebsiteLoginAdmin(UserAdmin):
    add_form = WebsiteLoginCreationForm
    form = WebsiteLoginChangeForm
    model = WebsiteLogin
    list_display = ['email', 'username']


class WebsiteLoginInline(admin.StackedInline):
    model = WebsiteLogin


class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'age']
    list_display_links = ['name', 'last_name']
    exclude = []
    inlines = [WebsiteLoginInline]
    prepopulated_fields = {'permalink': ('first_name', 'middle_name', 'last_name')}

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'children':
            kwargs['queryset'] = Member.objects.filter(role='S')
        return super().formfield_for_manytomany(db_field, request, **kwargs)


class ContributorAdmin(MemberAdmin):
    list_display = ['name', 'last_name']


class ParentAdmin(MemberAdmin):
    list_display = ['name', 'last_name']


class ScoutAdmin(MemberAdmin):
    exclude = ['children']
    inlines = []


admin.site.register(WebsiteLogin, WebsiteLoginAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Contributor, ContributorAdmin)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Scout, ScoutAdmin)
