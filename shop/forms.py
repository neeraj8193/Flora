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
        fields = '__all__'
        widgets = {
            'profile_img' : FileInput(),
        }


class EditProfileForm(forms.Form):
    username = forms.CharField()
    about_me = forms.CharField(widget=forms.Textarea())
    image = forms.ImageField(required=False)

    def __init__(self, original_username, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.original_username = original_username

    def clean_username(self):
        """
        This function throws an exception if the username has already been 
        taken by another user
        """

        username = self.cleaned_data['username']
        if username != self.original_username:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError(
                    'A user with that username already exists.')
        return username