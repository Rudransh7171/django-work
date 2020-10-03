from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
    english = models.CharField(max_length=100)
