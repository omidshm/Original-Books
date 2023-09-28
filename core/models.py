from django.contrib.auth.models import AbstractUser
from django.db import models

class AppUser(AbstractUser):
    email = models.EmailField(unique=True, null=True)


# The rest of your Core app models can go here if needed.
