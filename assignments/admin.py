from django.contrib import admin

from .models import Committee, Den


class CommitteePageInline(admin.StackedInline):
    model = Committee.page.through
    extra = 0
    verbose_name = 'web page'
    verbose_name_plural = 'web pages'


class CommitteeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'permalink': ('name', )}
    exclude = ['page']
    inlines = [CommitteePageInline]


class DenPageInline(admin.StackedInline):
    model = Den.page.through
    extra = 0
    verbose_name = 'web page'
    verbose_name_plural = 'web pages'


class DenAdmin(admin.ModelAdmin):
    list_display = ('number', 'rank')
    list_filter = ('rank', )
    exclude = ['page']
    inlines = [DenPageInline]


admin.site.register(Committee, CommitteeAdmin)
admin.site.register(Den, DenAdmin)
