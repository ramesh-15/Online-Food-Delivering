from django import forms
from django.forms import Select,ValidationError
from .models import DonarUser,Contact,Clothes
from django.core import validators
from django.contrib.auth.forms import UserCreationForm,UserChangeForm


class logform(forms.Form):
    username = forms.CharField(max_length=200)
    passcode = forms.CharField(max_length=200)


class regform(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    username = forms.CharField(max_length=200)
    email = forms.CharField(max_length=200)


        

class changepwd(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

class userform(UserChangeForm):
    password = None
    class Meta:
        model = DonarUser
        # fields = ['first_name', 'last_name', 'username', 'email']
        fields = '__all__'

# donate food
class donateform(forms.Form):
    food_name = forms.CharField(error_messages={'required':'Enter food name '})
    option = (('VEG', 'VEG'), ('NON-VEG', 'NON-VEG'))
    food_type = forms.ChoiceField(choices=option)
    quantity = forms.IntegerField()
    donar_contact = forms.CharField(max_length=10)
    pick_up = forms.CharField(max_length=200)
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
# clothes
class ClothesForm(forms.Form):
    Name = forms.CharField(error_messages={'required':'Enter clothes name '})
    option = (('WomenWare', 'WomenWare'), ('Kidsware', 'Kidsware'),('Menware', 'Menware'))
    catogiry = forms.ChoiceField(choices=option)
    pairs = forms.IntegerField()
    donar_contact = forms.CharField(max_length=10)
    pick_up = forms.CharField(max_length=200)
    pincode = forms.CharField(max_length=6)

# Health
class HealthForm(forms.Form):
    drugname = forms.CharField(error_messages={'required':'Enter drug name '})
    option = (('Polio Drops', 'Polio Drops'), ('Insulin', 'Insulin'),('tetanus ', 'tetanus '),('Covishield vaccine ', 'Covishield vaccine '),('Others ', 'Others '))
    catogiry = forms.ChoiceField(choices=option)
    quantity = forms.IntegerField()
    donar_contact = forms.CharField(max_length=10)
    pick_up = forms.CharField(max_length=200)
    pincode = forms.CharField(max_length=6)

# Footware
class FootwareForm(forms.Form):
    name = forms.CharField(error_messages={'required':'Enter footware name '})
    option =  (('WomenWare', 'WomenWare'), ('Kidsware', 'Kidsware'),('Menware', 'Menware'))
    catogiry = forms.ChoiceField(choices=option)
    pairs = forms.IntegerField()
    donar_contact = forms.CharField(max_length=10)
    pick_up = forms.CharField(max_length=200)
    pincode = forms.CharField(max_length=6)

class contactform(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Example@gmail.com'}))
    phone = forms.CharField(max_length=10)
    subject = forms.CharField(max_length=100,widget=forms.Textarea(attrs={'rows':1,'cols':25}))
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':5,'cols':25}))


    def clean_name(self):
        cleaned_data = super().clean()
        name = cleaned_data['name']
        if len(name)<=3:
            raise forms.ValidationError('Characters should be more than 3')

        return name

    def clean_phone(self):
        data = super().clean()
        ph = data['phone']
        if len(ph)!=10:
            raise forms.ValidationError('Please enter valid 10 digit mobile number...')
        elif ph[0] in '012345':
            raise forms.ValidationError('Number must be starts with 6,7,8,9')
        return ph



        
        
