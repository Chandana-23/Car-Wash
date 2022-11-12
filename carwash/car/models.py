from django.db import models

# Create your models here.

class Places(models.Model):
    place_name = models.CharField(max_length=250)

class Services(models.Model):
    service_name = models.CharField(max_length=250)