from django.contrib import admin

from .models import Committee


class PageInline(admin.StackedInline):
    model = Committee.page.through
    extra = 0
    verbose_name = 'web page'
    verbose_name_plural = 'web pages'


class CommitteeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'permalink': ('name',)}
    exclude = ['page']
    inlines = [PageInline]


admin.site.register(Committee, CommitteeAdmin)
