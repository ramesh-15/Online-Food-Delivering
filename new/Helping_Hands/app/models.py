import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils import timezone



DISCOUNT_CODE_TYPES_CHOICES = [
    ('percent', 'Percentage-based'),
    ('value', 'Value-based'),
]


# Create your models here
class MyUserManager(BaseUserManager):
    def create_user(self, email,  password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,  password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    user = (
      ('is_Donar', 'is_Donar'),
        ('is_Volunteer', 'is_Volunteer'),)
    options = models.CharField(max_length=100, choices=user, default=False)
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )
    gendar = models.CharField(max_length=100, choices=GENDER_CHOICES,default=False)
    ch = (
        ('Scribes', 'Scribes'),
        ('AnimalHusbandry', 'AnimalHusbandry'),
        ('MedicalCamp', 'MedicalCamp'),
        ('Devilery', 'Devilery')
    )
    AreaOfInterest = models.CharField(max_length=100, choices=ch,default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


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


# admin
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=100)


class MedicalCamp_event(models.Model):
    Organiser_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    camp_starts_at = models.CharField(max_length=100)
    camp_ends_at = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    possibilities=(('Children','Children'),("middle age",'middle age'),('old age','old age') ,('all','all'))
    For_whom = models.CharField(max_length=100,choices=possibilities)
    facilities = models.CharField(max_length=500)
    message = models.CharField(max_length=100)
    def __str__(self):
        return self.Organiser_name

class Bloodcamp_event(models.Model):
    Organisername = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    camp_starts_at = models.CharField(max_length=100)
    camp_ends_at = models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    def __str__(self):
        return self.Organisername


class Educational_event(models.Model):
    Organisername = models.CharField(max_length=100)
    poss=(('workshops','workshops'),('training sessions','training sessions'),('classes','classes '),('job_mela','job_mela'))
    category =models.CharField(max_length=50,choices=poss)
    Topic = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    camp_starts_at = models.CharField(max_length=100)
    camp_ends_at = models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    def __str__(self):
        return self.Organisername
    #Community_building_event

#Community-building events such as festivals, fairs, and cultural celebrations that promote social cohesion and a sense of belonging.

class CBEmodel(models.Model):
    Organisername = models.CharField(max_length=100)
    poss = (('festivals', 'festivals'), ('fairs', 'fairs'), ('cultural celebrations', 'cultural celebrations '))
    category=models.CharField(max_length=50,choices=poss)
    topic=models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    camp_starts_at = models.CharField(max_length=100)
    camp_ends_at = models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    def __str__(self):
        return self.Organisername


class AnimalCampModel(models.Model):
    Organisername = models.CharField(max_length=100)
    poss = (('for dogs', 'for dogs'), ('for Goats and sheeps', ' for Goats and sheeps'), ('for cattles', 'for cattles '), ('for birds', 'for birds'),('for all', 'for all'))
    category=models.CharField(max_length=100,choices=poss)
    place = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    camp_starts_at = models.CharField(max_length=100)
    camp_ends_at = models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    def __str__(self):
        return self.Organisername

class ForScribersModel(models.Model):
    Organisername = models.CharField(max_length=100)
    purpose=models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    camp_starts_at = models.CharField(max_length=100)
    camp_ends_at = models.CharField(max_length=100)
    date=models.CharField(max_length=100)
    contacts = models.CharField(max_length=100)
    def __str__(self):
        return self.Organisername
    