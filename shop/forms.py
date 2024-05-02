from django import forms
from .models import *
from django.forms.models import ModelForm
from django.forms.widgets import FileInput

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address_line_1','address_line_2','landmark','city','state','pincode']


class ProfileForm(ModelForm):
     class Meta:
        model = Profile
        fields = ['email','phone','address','about','image']


class VendorProfileForm(ModelForm):
     class Meta:
        model = VendorProfile
        fields = ['email','phone','address','about','image']