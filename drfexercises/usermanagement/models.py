from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    display_name = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
