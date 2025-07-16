from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    bio: models.TextField = models.TextField(max_length = 2048, blank = True, null = True)
    email: models.EmailField = models.EmailField(unique = True, blank = False, null = False )

    def __str__(self) -> str:
        return self.username