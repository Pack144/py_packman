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


class HomePage(Page):
    title = 'Home Page'
    permalink = 'home'

    def __str__(self):
        return 'Home page'

    def save(self, *args, **kwargs):
        if HomePage.objects.exists() and not self.pk:
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError('There is can be only one Homepage instance')
        return super(HomePage, self).save(*args, **kwargs)


class AboutPage(Page):
    title = 'About Us'
    permalink = 'about-us'

    def __str__(self):
        return 'About Us page'

    def save(self, *args, **kwargs):
        if AboutPage.objects.exists() and not self.pk:
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError('There is can be only one About Us instance')
        return super(AboutPage, self).save(*args, **kwargs)


class DynamicPage(Page):
    category = models.ManyToManyField(Category, related_name='pages')
    permalink = models.SlugField(unique=True)

    def __str__(self):
        return self.title
