from django.db import models


class Category(models.Model):
    name = models.TextField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "categories"


class Page(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    post_date = models.DateField()
    attachment = models.FileField(upload_to='pages/', null=True, blank=True)
    category = models.ManyToManyField(Category)
    permalink = models.SlugField(unique=True)

    def __str__(self):
        return self.title
