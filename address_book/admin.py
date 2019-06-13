from django.contrib import admin

from .models import Address, PhoneNumber, Venue, VenueType


class AddressAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': (('street', 'street2'), ('city', 'state', 'zip_code'))}),
        ('Permissions', {'fields': ('published',)}),
    )


class PhoneNumberAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {'fields': ('type', 'number')}),
        ('Permissions', {'fields': ('published',)}),
    )


admin.site.register(Address, AddressAdmin)
admin.site.register(PhoneNumber, PhoneNumberAdmin)
admin.site.register(Venue)
admin.site.register(VenueType)
