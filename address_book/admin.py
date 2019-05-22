from django.contrib import admin

from .models import Address, PhoneNumber, Venue, VenueType


class AddressAdmin(admin.ModelAdmin):
    fields: ('street', ('city', 'state', 'zip_code'))


admin.site.register(Address, AddressAdmin)
admin.site.register(PhoneNumber)
admin.site.register(Venue)
admin.site.register(VenueType)
