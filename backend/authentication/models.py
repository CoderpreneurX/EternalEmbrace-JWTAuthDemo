from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_user')
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f'{self.user.username} Profile'