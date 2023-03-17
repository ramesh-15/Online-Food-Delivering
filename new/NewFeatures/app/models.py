from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta,date
# Create your models here.




class DonarUser(models.Model):
    first_name = models.CharField(max_length=200,default='')
    last_name = models.CharField(max_length=200,default='')
    username = models.CharField(max_length=200,default='')
    email = models.CharField(max_length=200,default='')
    city = models.CharField(max_length=200,default='')
    state = models.CharField(max_length=200,default='')
    passcode = models.CharField(max_length=200,default='')


class Users_donations(models.Model) :
    food_name=models.CharField(max_length=100,verbose_name='Food Name')
    possibilities = (('VEG', 'VEG'), ('NON-VEG', 'NON-VEG'))
    food_type = models.CharField(max_length=100, choices=possibilities)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    donar_contact = models.CharField(max_length=10)
    food_pick_up = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    flag = models.CharField(max_length=12,default=False)
    flagreq = models.CharField(max_length=12,default=False)
    donarMail = models.EmailField(max_length=100,default='')
    message = models.TextField(max_length=300,default='')
    ngomessage = models.TextField(max_length=300,default='')
    donar_name = models.CharField(max_length=200,default='')
    ngo_name = models.CharField(max_length=200,default='')

    def __str__(self):
        return  ( self.food_name )
class Contact(models.Model): 
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

class Clothes(models.Model) :
    Name=models.CharField(max_length=100,verbose_name='Food Name')
    possibilities = (('WomenWare', 'WomenWare'), ('Kidsware', 'Kidsware'),('Menware', 'Menware'))
    catogiry = models.CharField(max_length=100, choices=possibilities)
    pairs = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    donar_contact = models.CharField(max_length=10)
    food_pick_up = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    flag = models.CharField(max_length=12,default=False)
    flagreq = models.CharField(max_length=12,default=False)
    donarMail = models.EmailField(max_length=100,default='')
    message = models.TextField(max_length=300,default='')
    ngomessage = models.TextField(max_length=300,default='')
    donar_name = models.CharField(max_length=200,default='')
    ngo_name = models.CharField(max_length=200,default='')

    def __str__(self):
        return  ( self.Name )
    
# Health
class Health(models.Model) :
    drugname=models.CharField(max_length=100,verbose_name='Food Name')
    possibilities = (('Polio Drops', 'Polio Drops'), ('Insulin', 'Insulin'),('tetanus ', 'tetanus '),('Covishield vaccine ', 'Covishield vaccine '),('Others ', 'Others '))
    catogiry = models.CharField(max_length=100, choices=possibilities)
    quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    donar_contact = models.CharField(max_length=10)
    food_pick_up = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    flag = models.CharField(max_length=12,default=False)
    flagreq = models.CharField(max_length=12,default=False)
    donarMail = models.EmailField(max_length=100,default='')
    message = models.TextField(max_length=300,default='')
    ngomessage = models.TextField(max_length=300,default='')
    donar_name = models.CharField(max_length=200,default='')
    ngo_name = models.CharField(max_length=200,default='')

    def __str__(self):
        return  ( self.drugname)
    
# Footware
class Footware(models.Model) :
    name=models.CharField(max_length=100,verbose_name='Food Name')
    possibilities =(('WomenWare', 'WomenWare'), ('Kidsware', 'Kidsware'),('Menware', 'Menware'))
    catogiry = models.CharField(max_length=100, choices=possibilities)
    pairs = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    donar_contact = models.CharField(max_length=10)
    food_pick_up = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    flag = models.CharField(max_length=12,default=False)
    flagreq = models.CharField(max_length=12,default=False)
    donarMail = models.EmailField(max_length=100,default='')
    message = models.TextField(max_length=300,default='')
    ngomessage = models.TextField(max_length=300,default='')
    donar_name = models.CharField(max_length=200,default='')
    ngo_name = models.CharField(max_length=200,default='')

    def __str__(self):
        return  ( self.name)