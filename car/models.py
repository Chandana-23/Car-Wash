from django.db import models

# Create your models here.

class Places(models.Model):
    place_name = models.CharField(max_length=250)

class Services(models.Model):
    service_name = models.CharField(max_length=250)

class Members(models.Model):
    username = models.CharField(max_length=250,primary_key=True)
    password = models.CharField(max_length=250)

class Booking(models.Model):
    service = models.CharField(max_length=250,default='')
    place = models.CharField(max_length=250,default='')
    approval = models.CharField(max_length=250,choices=[('S','Success'),('P','Pending'),('R','Rejected')],default="P")
    username = models.CharField(max_length=250,default='')