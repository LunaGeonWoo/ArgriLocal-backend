from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    address = models.CharField(
        max_length=200,
        verbose_name="주소",
    )
    first_name = models.CharField(
        max_length=150,
        editable=False,
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=150,
        default="",
        verbose_name="이름",
    )
