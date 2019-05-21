from django.db import models
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class DynamicPage(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    post_datetime = models.DateTimeField(auto_now_add=True)
    attachment = models.FileField(upload_to='pages/', null=True, blank=True)
    category = models.ManyToManyField(Category, related_name='pages')
    permalink = models.SlugField(unique=True)

    def __str__(self):
        return self.title
