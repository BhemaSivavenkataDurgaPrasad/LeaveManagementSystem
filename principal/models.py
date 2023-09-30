from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class principle(models.Model) :
    Name = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Phone = models.CharField(max_length=10)
    Address = models.CharField(max_length=50)
    