from django import forms
from django.forms import Select,ValidationError
from .models import User,Contact,food_requests
from django.core import validators
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class logform(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','autocomplete': 'off','autofocus': 'autofocus','size': '40','font-size': 'xx-large'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','size': '15'}))

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
        # fields = ['first_name', 'last_name', 'username', 'email']
        fields = '__all__'

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

# request food NGO
class NGO_request(forms.ModelForm):
    class Meta:
        model = food_requests
        
        fields = ['food_id','food_name','username','pickup_point','donar_contact']
        
        
