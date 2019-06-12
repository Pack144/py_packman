from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from assignments.models import Committee, Den
from address_book.models import Address, PhoneNumber, Venue

from . import managers


class Member(models.Model):
    """Base object defining a member of the pack. Examples include a parent/guardian, cub scout, or contributor."""
    first_name = models.CharField(max_length=32)
    nickname = models.CharField(max_length=32, blank=True, null=True)
    middle_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=64)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)
    active = models.BooleanField(default=True)
    accepted_into_the_pack = models.BooleanField(default=False)

    ROLE_CHOICES = (
        ('S', 'Cub'),
        ('P', 'Parent/Guardian'),
        ('C', 'Contributor'),
    )
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, blank=True, null=True)

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Prefer not to say'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='U')

    # Useful information for parents and contributors
    children = models.ManyToManyField('self', related_name='parents', symmetrical=False, blank=True)
    committee_leadership = models.ManyToManyField(Committee, blank=True, related_name='membership')
    den_leadership = models.ManyToManyField(Den, blank=True, related_name='leadership')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True, related_name='member_address')
    phone_number = models.ManyToManyField(PhoneNumber, blank=True, related_name='member_phone')

    # Useful information for cubs
    den_assigned = models.ForeignKey(Den, on_delete=models.CASCADE, null=True, blank=True, related_name='membership')
    school = models.ForeignKey(Venue, on_delete=models.CASCADE, null=True, blank=True, related_name='school_member')

    date_added = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    permalink = models.SlugField(null=False, unique=True)

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


class Login(AbstractUser):
    """If the member is allowed to log into the website, this class will store their credentials."""
    username = None
    email = models.EmailField(_('email address'), unique=True)
    subscribed = models.BooleanField(default=True, help_text='Allow email communication from the website.')
    published = models.BooleanField(default=True, help_text='Display your email address to other members of the pack.')
    member = models.OneToOneField(Member, on_delete=models.CASCADE, blank=True, null=True, related_name='login')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = managers.LoginManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        if self.member:
            return self.member.name
        else:
            return self.email

    class Meta:
        verbose_name = 'web login'
        verbose_name_plural = 'web login'


class Contributor(Member):
    objects = managers.ContributorManager()

    class Meta:
        proxy = True


class Parent(Member):
    objects = managers.ParentManager()

    class Meta:
        proxy = True


class Scout(Member):
    objects = managers.ScoutManager()

    class Meta:
        proxy = True
