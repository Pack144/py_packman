from django.contrib import admin

from .models import Address, PhoneNumber


class AddressAdmin(admin.ModelAdmin):
    fields: ('street', ('city', 'state', 'zip_code'))


admin.site.register(Address, AddressAdmin)
admin.site.register(PhoneNumber)
