from django.db import models

# Create your models here.
class DonarUser(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    passcode = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

class Food(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


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
    
