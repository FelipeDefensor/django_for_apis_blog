from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Custom user model"""
    name = models.CharField(null=True, blank=True, max_length=100)



# Create your models here.
