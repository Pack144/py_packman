from django.db import models


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
        return '{}, {}, {}, {}'.format(self.street, self.city, self.state, self.zip_code)


class PhoneNumber(models.Model):
    number = models.CharField(max_length=16)
    TYPE_CHOICES = (
        ('H', 'Home'),
        ('M', 'Mobile'),
        ('W', 'Work'),
        ('F', 'Fax'),
        ('O', 'Other')
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)

    date_added = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.number)


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
