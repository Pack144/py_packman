from django.contrib.auth.models import AbstractUser
from django.db import models


class Member(AbstractUser):

    def __str__(self):
        return self.email
