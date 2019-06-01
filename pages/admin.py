from django.contrib import admin

from . import models


class StaticPageAdmin(admin.ModelAdmin):
    fields = ('page', 'body')


class CategoryInline(admin.TabularInline):
    model = models.DynamicPage.category.through
    extra = 0
    verbose_name = 'category'
    verbose_name_plural = 'categories'


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'permalink': ('title', )}
    list_display = ('title', 'post_datetime', )
    list_filter = ('category',)
    search_fields = ['title', 'category', 'post_datetime']
    inlines = [CategoryInline]
    exclude = ['category']


admin.site.register(models.StaticPage, StaticPageAdmin)
admin.site.register(models.DynamicPage, PageAdmin)
admin.site.register(models.Category)
