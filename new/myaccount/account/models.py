from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta,date
# Create your models here.

class User(AbstractUser):
    is_Donar = models.BooleanField('Donar',default='')
    is_NGO = models.BooleanField('NGO',default='')


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
    donarMail = models.EmailField(max_length=100,default='')

    def __str__(self):
        return  ( self.food_name )
class Contact(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)

class food_requests(models.Model):
    food_id = models.ForeignKey(Users_donations, on_delete=models.CASCADE)    
    username = models.CharField(max_length=100) 
    food_name=models.CharField(max_length=100)    
    pickup_point=models.CharField(max_length=100)    
    donar_contact=models.CharField(max_length=100)    
    date = models.DateField(default=date.today()) 
    def __str__(self):        
        return self.username