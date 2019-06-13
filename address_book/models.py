from django.db import models

from localflavor.us.models import USStateField, USZipCodeField
from phonenumber_field.modelfields import PhoneNumberField


class Address(models.Model):
    street = models.CharField(max_length=128)
    street2 = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=64)
    state = USStateField()
    zip_code = USZipCodeField()

    published = models.BooleanField(default=True, help_text='Display your address to other members of the pack.')

    date_added = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'addresses'

    def __str__(self):
        if not self.street2:
            return '{}, {} {}, {}'.format(self.street, self.city, self.state, self.zip_code)
        else:
            return '{} {}, {} {}, {}'.format(self.street, self.street2, self.city, self.state, self.zip_code)


class PhoneNumber(models.Model):
    number = PhoneNumberField()
    TYPE_CHOICES = (
        ('H', 'Home'),
        ('M', 'Mobile'),
        ('W', 'Work'),
        ('F', 'Fax'),
        ('O', 'Other')
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    published = models.BooleanField(default=True, help_text='Display this phone number to other members of the pack.')

    date_added = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number.as_national


class VenueType(models.Model):
    type = models.CharField(max_length=16, help_text='e.g. School, Campground, Park, etc.')

    date_added = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.type


class Venue(models.Model):
    name = models.CharField(max_length=128, unique=True)
    type = models.ForeignKey(VenueType, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE, null=True, blank=True, related_name='venue')
    phone_number = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE, null=True, blank=True, related_name='venue')

    date_added = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
