from django.db import models
from django.urls import reverse

from pages.models import Page


class Committee(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    page = models.ManyToManyField(Page, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    permalink = models.SlugField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('committee-detail', args=[str(self.permalink)])
