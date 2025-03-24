from django import forms
from django.forms import ModelForm
from.models import Venue


class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'phone', 'web', 'email_address')
        labels = {
            'name': '',
            'address': '',
            'zip_code': '',
            'phone': '',
            'web': '',
            'email_address': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Venue name'}),
            'address': forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Venue address'}),
            'zip_code': forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'zip code'}),
            'phone': forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'phone'}),
            'web' :forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'web address'}),
            'email_address': forms.EmailInput(attrs={'class' : 'form-control', 'placeholder':'email'}),

        }