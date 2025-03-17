from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.language.models import Language


class User(AbstractUser):
    language = models.ForeignKey(Language, on_delete=models.PROTECT, null=True, blank=True)

    REQUIRED_FIELDS = ['language']