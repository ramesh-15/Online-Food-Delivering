from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin



# class User(AbstractBaseUser, PermissionsMixin):
#     passcode = models.CharField(max_length=100,default='')
#     password = models.CharField(max_length=100,default='')
#     user = (
#         ('is_Donar', 'is_Donar'),
#         ('is_Volunteer', 'is_Volunteer'),)
#     options = models.CharField(max_length=100, choices=user, default=False)
#     GENDER_CHOICES = (
#         ('Male', 'Male'),
#         ('Female', 'Female'),
#         ('Others', 'Others')
#     )
#     gender = models.CharField(max_length=100, choices=GENDER_CHOICES,default=False)

class Users_donations(models.Model) :
    name=models.CharField(max_length=100,verbose_name='name')
    possibilities = (('VEG', 'VEG'), ('NON-VEG', 'NON-VEG'))
    food_type = models.CharField(max_length=100, choices=possibilities)
    md = (('Polio', 'Polio'), ('Others', 'Others'))
    medine_type = models.CharField(max_length=100, choices=md)
    gd = (('Male', 'Male'), ('Female', 'Female'))
    gender = models.CharField(max_length=100, choices=gd)
    quantity = models.CharField(max_length=100,default='0')
    date = models.DateTimeField(auto_now_add=True)
    exp = models.DateTimeField()
    contact = models.CharField(max_length=10)
    pick_up = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    donar_name = models.CharField(max_length=200,default='')
    flag = models.CharField(max_length=12,default=False)

    