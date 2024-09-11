from django.contrib.auth.models import AbstractUser
from django.db import models

from app.constants import NULLABLE


class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True, verbose_name='email')
    avatar = models.ImageField(upload_to='users/', **NULLABLE, verbose_name='Avatar')
    city = models.CharField(max_length=100, **NULLABLE, verbose_name='City')
    phone = models.CharField(max_length=50, **NULLABLE, verbose_name='Number phone')
    age = models.PositiveIntegerField(verbose_name='Age')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
