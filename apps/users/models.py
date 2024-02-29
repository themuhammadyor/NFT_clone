from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.shared.models import AbstractModel


# Create your models here.

class User(AbstractUser, AbstractModel):
    avatar = models.ImageField(upload_to="users/avatar/%Y/%m/%d", default="user_avatar.jpg")
