from django.db import models

# Create your models here.
class DonarUser(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    passcode = models.CharField(max_length=200)
    new_password = models.CharField(max_length=200,default='')
    confirm_password = models.CharField(max_length=200,default='')
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

# class LoginDetials(models.Model):
#     username = models.CharField(max_length=100)
#     login_data = models.DateTimeField(auto_now_add=True)
#     logout_data = models.DateTimeField(auto_now_add=True)

# class Food(models.Model):
#     name = models.CharField(max_length=100)
#     quantity = models.PositiveIntegerField()
#     pair = models.PositiveIntegerField()
#     possibilities = (('WomenWare', 'WomenWare'), ('Kidsware', 'Kidsware'),('Menware', 'Menware'))
#     catogiry = models.CharField(max_length=100, choices=possibilities)
#     medine = (('Polio Drops', 'Polio Drops'), ('Insulin', 'Insulin'),('tetanus ', 'tetanus '),('Covishield vaccine ', 'Covishield vaccine '),('Others ', 'Others '))
#     catogiry = models.CharField(max_length=100, choices=medine)
#     expr = models.CharField(max_length=100)
#     contact = models.CharField(max_length=100)
#     address = models.CharField(max_length=100)


class Users_donations(models.Model) :
    name=models.CharField(max_length=100,verbose_name='name')
    possibilities = (('VEG', 'VEG'), ('NON-VEG', 'NON-VEG'))
    food_type = models.CharField(max_length=100, choices=possibilities)
    md = (('Polio', 'Polio'), ('Others', 'Others'))
    medine_type = models.CharField(max_length=100, choices=md)
    gd = (('Male', 'Male'), ('Female', 'Female'))
    gender = models.CharField(max_length=100, choices=gd)
    quantity = models.PositiveIntegerField(default='')
    date = models.DateTimeField(auto_now_add=True)
    exp = models.DateTimeField()
    contact = models.CharField(max_length=10)
    pick_up = models.CharField(max_length=200)
    pincode = models.CharField(max_length=6)
    donar_name = models.CharField(max_length=200,default='')
    flag = models.CharField(max_length=12,default=False)
    # flagreq = models.CharField(max_length=12,default=False)
    # donarMail = models.EmailField(max_length=100,default='')
    # message = models.TextField(max_length=300,default='')
    
    


    def __str__(self):
        return  ( self.name )
    
