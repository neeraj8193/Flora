from django import forms
from .models import *

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address_line_1','address_line_2','landmark','city','state','pincode']
