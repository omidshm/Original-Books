from django.contrib.auth.models import AbstractUser
from django.db import models

class AppUser(AbstractUser):
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

# The rest of your Core app models can go here if needed.
