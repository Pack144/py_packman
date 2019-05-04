from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class WebsiteLogin(AbstractUser):

    def __str__(self):
        return self.email


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


class Family(models.Model):
    family_name = models.CharField(max_length=150, unique=True)

    class Meta:
        verbose_name = 'Family'
        verbose_name_plural = 'Families'

    def __str__(self):
        return self.family_name


class Member(models.Model):
    first_name = models.CharField(max_length=32)
    nickname = models.CharField(max_length=32, blank=True, null=True)
    middle_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    children = models.ManyToManyField('self', related_name='parents', symmetrical=False, blank=True)

    CUB = 'S'
    GUARDIAN = 'G'
    CONTRIBUTOR = 'C'
    WAITLIST = 'W'
    ROLE_CHOICES = (
        (CUB, 'Cub'),
        (GUARDIAN, 'Guardian'),
        (CONTRIBUTOR, 'Contributor'),
        (WAITLIST, 'Wait list'),
    )
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default=WAITLIST)

    class Meta:
        verbose_name = 'member'
        verbose_name_plural = 'members'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return self.get_short_name()

    def get_age(self):
        if not self.date_of_birth:
            return None
        today = timezone.now()
        return today.year - self.date_of_birth.year - (
                    (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    def get_full_name(self):
        return "{} {}".format(self.get_short_name(), self.last_name).strip()

    def get_parents(self):
        return self.parents.all()

    def get_short_name(self):
        if self.nickname:
            return self.nickname.strip()
        else:
            return self.first_name.strip()
