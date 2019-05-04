from django.contrib.auth.models import AbstractUser
from django.db import models


class WebsiteLogin(AbstractUser):

    def __str__(self):
        return self.email


class Role(models.Model):
    """
    The Role entries are managed by the system,
    automatically created via a Django data migration.
    """
    CUB = 1
    GUARDIAN = 2
    CONTRIBUTOR = 3
    WAITLIST = 4
    ROLE_CHOICES = (
        (CUB, 'cub'),
        (GUARDIAN, 'guardian'),
        (CONTRIBUTOR, 'contributor'),
        (WAITLIST, 'waitlist'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


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
    first_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, blank=True, null=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)
    user_type = models.ManyToManyField(Role, default='waitlist')
    family = models.ForeignKey(Family, on_delete=models.CASCADE, null=True, blank=True)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    class Meta:
        verbose_name = 'member'
        verbose_name_plural = 'members'

    def __str__(self):
        return self.get_short_name()

    def get_full_name(self):
        if self.nickname:
            return "{} {}".format(self.nickname, self.last_name).strip()
        else:
            return "{} {}".format(self.first_name, self.last_name).strip()

    def get_short_name(self):
        if self.nickname:
            return self.nickname.strip()
        else:
            return self.first_name.strip()
