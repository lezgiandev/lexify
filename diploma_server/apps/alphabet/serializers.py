from rest_framework import serializers
from apps.alphabet.models import Letter


class LetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Letter
        fields = ('id', 'letter', 'letter', 'audio')