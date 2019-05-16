from django.contrib import admin
from .models import Category
from .models import Page


class CategoryInline(admin.TabularInline):
    model = Page.category.through
    extra = 0
    verbose_name = 'category'
    verbose_name_plural = 'categories'


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"permalink": ("title", )}
    list_display = ('title', 'post_date', )
    list_filter = ('category',)
    search_fields = ['title', 'category', ]
    inlines = [CategoryInline]
    exclude = ['category']


admin.site.register(Category)
admin.site.register(Page, PageAdmin)
