from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    school_name = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)
    

    def __str__(self):
        return self.username

