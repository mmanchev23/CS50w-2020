from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Workout(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(max_length=255)
    savedInProfile = models.BooleanField(default=False)

    def __str__(self):
        return self.name