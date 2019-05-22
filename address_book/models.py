from django.db import models

from phonenumber_field.modelfields import PhoneNumberField


class Address(models.Model):
    street = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)

    date_added = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'addresses'

    def __str__(self):
        return {}, {}, {}, {}.format(self.street, self.city, self.state, self.zip_code)


class PhoneNumber(models.Model):
    number = PhoneNumberField()

    date_added = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.number)
