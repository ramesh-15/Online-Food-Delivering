from django.db import models

class DonarUser(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    passcode = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)