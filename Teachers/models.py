from datetime import datetime
from django.db import models
from django.core import validators
from django.contrib.auth.models import User

# Create your models here.
class userprofile(models.Model) :
    User = models.OneToOneField(User , on_delete=models.CASCADE)
    role = models.CharField(max_length=50)
     
class teacher(models.Model) :
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Phone = models.CharField(max_length=10)
    Address = models.CharField(max_length=50)

class leave(models.Model):
    Name = models.CharField(max_length=20)
    Grant = models.CharField(max_length=20 ,default = "not grant")
    Fdate = models.DateField(null=True)
    Tdata = models.CharField(max_length=10)
    Reasion = models.CharField(max_length=100 )
     

