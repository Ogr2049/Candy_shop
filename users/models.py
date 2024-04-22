from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    image = models.FileField(upload_to='user/image', blank=True, null=True,)
    weight = models.FloatField(default=60.0,)