from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class MembershipManager(UserManager):
    def create_user(self, email=None, password=None, **kwargs):
        """
        Creates and saves a User with the given email and password.
        """
        user = self.model(
            email=self.normalize_email(email),
        )

        for kwarg in kwargs:
            user.kwarg = kwarg

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password):
        """
        Creates and saves a staff user with the given email and password.
        """
        if not email:
            raise ValueError('Staff must have an email address')

        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        if not email:
            raise ValueError('Admins must have an email address')

        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user


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


class Member(AbstractUser):
    first_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=30, blank=True, null=True)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(blank=True, null=True)
    user_type = models.ManyToManyField(Role, default='waitlist')

    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']
    # objects = MembershipManager()

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
