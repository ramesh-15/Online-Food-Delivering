from django import forms
from .models import User
from django.core import validators
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class logform(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class regform(UserCreationForm):


    # option = (('M',"Male"),("F","Female"))
    # gender = forms.ChoiceField(widget=forms.RadioSelect(),choices=option)
    class Meta:
        model = User
        #fields =['is_Donar','is_NGO','dd_username','dd_email','phone_number','donation_from','address','pincode','city','state']
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'is_Donar', 'is_NGO']

class changepwd(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

class userform(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

# donate food
class donateform(forms.Form):
    food_name = forms.CharField(error_messages={'required':'Enter food name '})
    option = (('VEG', 'VEG'), ('NON-VEG', 'NON-VEG'))
    food_type = forms.ChoiceField(choices=option)
    quantity = forms.IntegerField()
    donar_contact = forms.CharField(max_length=10)
    food_pick_up = forms.CharField(max_length=200)
    pincode = forms.CharField(max_length=6)

    def clean_food_name(self):
        cleaned_data = super().clean()
        n = cleaned_data['food_name']
        if len(n)<=3:
            raise forms.ValidationError('enter valid item name')
        return n

        # def cleaned_Contact(self):
        #     cleaned_data = super().clean()
        #     mb = cleaned_data['Contact']
        #     if len(mb) < 10 and (mb[0] == 9 or mb[0] == 8 or mb[0] == 7):
        #         raise forms.ValidationError('enter proper mobile number')
        #     return mb