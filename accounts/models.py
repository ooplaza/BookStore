""" Whenever we call get_user_model() we will be linked up here. """

from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    pass
