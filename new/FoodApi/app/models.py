from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    is_Donar = models.BooleanField('Donar',null=False,default=False)
    is_NGO = models.BooleanField('NGO',null=False,default=False)

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
    
