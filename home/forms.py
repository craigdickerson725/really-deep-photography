from django import forms

class CheckoutForm(forms.Form):
    # Personal Information
    first_name = forms.CharField(max_length=50, required=True, label='First Name')
    last_name = forms.CharField(max_length=50, required=True, label='Last Name')
    email = forms.EmailField(required=True, label='Email Address')
    phone_number = forms.CharField(max_length=15, required=True, label='Phone Number')

    # Billing Address
    billing_address_1 = forms.CharField(max_length=100, required=True, label='Billing Address 1')
    billing_address_2 = forms.CharField(max_length=100, required=False, label='Billing Address 2')
    city = forms.CharField(max_length=50, required=True, label='City')
    state = forms.CharField(max_length=50, required=True, label='State/Province')
    zip_code = forms.CharField(max_length=10, required=True, label='Zip Code')
    country = forms.CharField(max_length=50, required=True, label='Country')

    # Shipping Address
    shipping_address_same = forms.BooleanField(required=False, label='Shipping address is the same as billing address')
    shipping_address_1 = forms.CharField(max_length=100, required=False, label='Shipping Address 1')
    shipping_address_2 = forms.CharField(max_length=100, required=False, label='Shipping Address 2')
    shipping_city = forms.CharField(max_length=50, required=False, label='Shipping City')
    shipping_state = forms.CharField(max_length=50, required=False, label='Shipping State/Province')
    shipping_zip_code = forms.CharField(max_length=10, required=False, label='Shipping Zip Code')
    shipping_country = forms.CharField(max_length=50, required=False, label='Shipping Country')

    # Method to get full billing name
    def get_billing_name(self):
        return f"{self.cleaned_data['first_name']} {self.cleaned_data['last_name']}"
