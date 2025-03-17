from django.db import models
from apps.language.models import Language


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Source(models.Model):
    text = models.CharField(max_length=255)
    link = models.CharField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    def __str__(self):
        return self.text


class MarkedSource(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user', 'source')
    def __str__(self):
        return f"{self.user.username} - {self.source.text}"