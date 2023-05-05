from django.db import models

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
    Date = models.DateField()
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
    date=models.DateField()
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
    date=models.DateField()
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
    date=models.DateField()
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
    date=models.DateField()
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
    date=models.DateField()
    contacts = models.CharField(max_length=100)
    def __str__(self):
        return self.Organisername