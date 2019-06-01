from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import forms, models


class LoginAdmin(UserAdmin):
    add_form = forms.LoginCreationForm
    form = forms.LoginChangeForm
    model = models.Login
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('email', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': (('email', 'subscribed', 'published' ), 'password', 'member')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': (('email', 'subscribed', 'published' ), 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )
    search_fields = ('email', )
    ordering = ('email', )


class LoginInline(admin.StackedInline):
    add_form = forms.LoginCreationForm
    form = forms.LoginChangeForm
    model = models.Login
    classes = ['collapse']
    fieldsets = (
        (None, {'fields': (('email', 'subscribed', 'published' ), 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')
        }),
    )


class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_name', 'age']
    list_display_links = ['name', 'last_name']
    list_filter = ['active', 'role']
    exclude = []
    inlines = [LoginInline]
    search_fields = ('first_name', 'nickname', 'middle_name', 'last_name', )
    prepopulated_fields = {'permalink': ('first_name', 'middle_name', 'last_name')}

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'children':
            kwargs['queryset'] = models.Member.objects.filter(role='S')
        return super().formfield_for_manytomany(db_field, request, **kwargs)


class ContributorAdmin(MemberAdmin):
    list_filter = ['active']
    list_display = ['name', 'last_name']


class ParentAdmin(MemberAdmin):
    list_filter = ['active']
    list_display = ['name', 'last_name']


class ScoutAdmin(MemberAdmin):
    list_filter = ['active', 'accepted_into_the_pack']
    exclude = ['children']
    inlines = []


admin.site.register(models.Login, LoginAdmin)
admin.site.register(models.Member, MemberAdmin)
admin.site.register(models.Contributor, ContributorAdmin)
admin.site.register(models.Parent, ParentAdmin)
admin.site.register(models.Scout, ScoutAdmin)
