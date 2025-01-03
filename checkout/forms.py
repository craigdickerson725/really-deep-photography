from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode', 'country',
                  'county',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels, and set autofocus on the first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Postal Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County, State, or Locality',
        }

        # Set autofocus on the first field
        self.fields['full_name'].widget.attrs['autofocus'] = True

        for field in self.fields:
            if field == 'postcode':
                self.fields[field].required = True
                self.fields['county'].required = True
            if field != 'country':
                # Add asterisk for required fields
                placeholder = f"{placeholders[field]} *" if self.fields[field].required else placeholders[field]  # noqa
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input larger-input'  # noqa
            # Remove labels for a cleaner form design
            self.fields[field].label = False
