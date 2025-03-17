from django.db import models
from apps.language.models import Language


class Letter(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    letter = models.CharField(max_length=100)
    audio = models.CharField(max_length=1000)