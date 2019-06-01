from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Page(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    post_datetime = models.DateTimeField(default=timezone.now)
    attachment = models.FileField(upload_to='pages/', null=True, blank=True)

    date_created = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class StaticPage(Page):
    title = None
    PAGE_CHOICES = (
        ('H', 'Home Page'),
        ('A', 'About Us'),
        ('L', 'Our History')
    )
    page = models.CharField(max_length=1, choices=PAGE_CHOICES, primary_key=True)

    class Meta:
        ordering = ['page']

    def __str__(self):
        return self.get_page_display()


class DynamicPage(Page):
    category = models.ManyToManyField(Category, related_name='pages')
    permalink = models.SlugField(unique=True)

    def __str__(self):
        return self.title
