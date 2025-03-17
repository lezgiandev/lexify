from django.db import models
from apps.language.models import Language


class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class PartOfSpeech(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Word(models.Model):
    text = models.CharField(max_length=50)
    part_of_speech = models.ForeignKey(PartOfSpeech, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return self.text


class Translation(models.Model):
    text = models.CharField(max_length=50)
    audio = models.CharField(max_length=1000)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.word.text} - {self.text}"
    class Meta:
        ordering = ['id']


class FavoriteWord(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    translation = models.ForeignKey(Translation, on_delete=models.CASCADE)
    class Meta:
        unique_together = ('user', 'translation')
    def __str__(self):
        return f"{self.user.username} - {self.translation.text}"