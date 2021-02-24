from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass

class Lead(models.Model):
    first_name = models.CharField(max_length=20, default=None)
    last_name = models.CharField(max_length=20, default=None)

class LeadAssigned(models.Model):
    pass

class LeadStatus(models.Model):
    pass