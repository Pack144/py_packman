from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils import timezone

from assignments.models import Committee, Den


class Member(models.Model):
    """Base object defining a member of the pack. Examples include a parent/guardian, cub scout, or contributor."""
    first_name = models.CharField(max_length=32)
    nickname = models.CharField(max_length=32, blank=True, null=True)
    middle_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=64)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)
    children = models.ManyToManyField('self', related_name='parents', symmetrical=False, blank=True)
    permalink = models.SlugField(null=False, unique=True)

    date_added = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    ROLE_CHOICES = (
        ('S', 'Cub'),
        ('P', 'Parent/Guardian'),
        ('C', 'Contributor'),
    )
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default='P')

    class Meta:
        verbose_name_plural = 'all members'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return self.full_name()

    def age(self):
        if not self.date_of_birth:
            return None
        today = timezone.now()
        return today.year - self.date_of_birth.year - (
                    (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    def full_name(self):
        return "{} {}".format(self.name(), self.last_name).strip()

    def parents(self):
        return self.parents.all()

    def name(self):
        if self.nickname:
            return self.nickname.strip()
        else:
            return self.first_name.strip()

    def get_absolute_url(self):
        return reverse('member-detail', args=[str(self.permalink)])


class WebsiteLogin(AbstractUser):
    """If the member is allowed to log into the website, this class will store their credentials."""
    member = models.OneToOneField(Member, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.email


class ContributorManager(models.Manager):
    def get_queryset(self):
        return super(ContributorManager, self).get_queryset().filter(role='C')


class Contributor(Member):
    objects = ContributorManager()

    class Meta:
        proxy = True


class ParentManager(models.Manager):
    def get_queryset(self):
        return super(ParentManager, self).get_queryset().filter(role='P')


class Parent(Member):
    objects = ParentManager()

    class Meta:
        proxy = True


class ScoutManager(models.Manager):
    def get_queryset(self):
        return super(ScoutManager, self).get_queryset().filter(role='S')


class Scout(Member):
    objects = ScoutManager()

    class Meta:
        proxy = True
