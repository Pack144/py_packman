from django.db import models
from django.urls import reverse

from pages.models import DynamicPage


class Rank(models.Model):
    BOBCAT = 1
    TIGER = 2
    WOLF = 3
    BEAR = 4
    JR_WEBE = 5
    SR_WEBE = 6
    ARROW = 7
    RANK_CHOICES = (
        (BOBCAT, "Bobcat"),
        (TIGER, "Tiger"),
        (WOLF, "Wolf"),
        (BEAR, "Bear"),
        (JR_WEBE, "Jr. Webelos"),
        (SR_WEBE, "Sr. Webelos"),
        (ARROW, "Arrow of Light"),
    )

    id = models.PositiveSmallIntegerField(choices=RANK_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class Committee(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    page = models.ManyToManyField(DynamicPage, blank=True, related_name='committee')
    date_added = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    permalink = models.SlugField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('committee-detail', args=[str(self.permalink)])


class Den(models.Model):
    number = models.PositiveIntegerField(primary_key=True)

    date_added = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    BOBCAT = 1
    TIGER = 2
    WOLF = 3
    BEAR = 4
    JR_WEBE = 5
    SR_WEBE = 6
    ARROW = 7
    RANK_CHOICES = (
        (BOBCAT, "Bobcat"),
        (TIGER, "Tiger"),
        (WOLF, "Wolf"),
        (BEAR, "Bear"),
        (JR_WEBE, "Jr. Webelos"),
        (SR_WEBE, "Sr. Webelos"),
        (ARROW, "Arrow of Light"),
    )

    rank = models.PositiveSmallIntegerField(choices=RANK_CHOICES, default=2)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return 'Den {}'.format(self.number)

    def get_absolute_url(self):
        return reverse('den-detail', args=[str(self.number)])

    def display_rank(self):
        return self.rank.get_id_display()

