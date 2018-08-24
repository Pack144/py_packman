from django.contrib import admin
from .models import Category
from .models import Page


class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {"permalink": ("title", )}
    list_display = ('title', 'post_date', )
    list_filter = ('category',)
    search_fields = ['title', 'category', ]


admin.site.register(Category)
admin.site.register(Page, PageAdmin)
