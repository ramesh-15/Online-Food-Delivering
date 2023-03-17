from .models import DonarUser
from django import forms


class DonarUserForm(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    username = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)
    city = forms.CharField(max_length=200)
    state = forms.CharField(max_length=200)


class Donarlogform(forms.Form):
    username = forms.CharField(max_length=200)
    passcode = forms.CharField(max_length=200)