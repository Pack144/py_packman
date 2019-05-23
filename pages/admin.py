from django.contrib import admin
from django.utils import timezone

from .models import Category, DynamicPage, AboutPage, HomePage


class CategoryInline(admin.TabularInline):
    model = DynamicPage.category.through
    extra = 0
    verbose_name = 'category'
    verbose_name_plural = 'categories'


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"permalink": ("title", )}
    list_display = ('title', 'post_datetime', )
    list_filter = ('category',)
    search_fields = ['title', 'category', 'post_datetime']
    inlines = [CategoryInline]
    exclude = ['category']


admin.site.register(Category)
admin.site.register(DynamicPage, PageAdmin)
admin.site.register(AboutPage)
admin.site.register(HomePage)
