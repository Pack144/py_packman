from django.forms import ModelForm

from .models import Address, PhoneNumber


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fieldsets = (
            (None, {'fields': ('street', 'street2', ('city', 'state', 'zip_code'))}),
            ('Permissions', {'fields': ('published',)}),
        )


class PhoneNumberForm(ModelForm):
    class Meta:
        model = PhoneNumber
        fieldsets = (
            (None, {'fields': ('type', 'number')}),
            ('Permissions', {'fields': ('published',)}),
        )
