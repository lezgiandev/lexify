from rest_framework import serializers
from .models import Category, Word, Translation, FavoriteWord, PartOfSpeech


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PartOfSpeechSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartOfSpeech
        fields = '__all__'


class WordSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    part_of_speech = PartOfSpeechSerializer()

    class Meta:
        model = Word
        fields = ('id', 'text', 'category', 'part_of_speech')


class TranslationSerializer(serializers.ModelSerializer):
    word = WordSerializer()
    language = serializers.StringRelatedField()

    class Meta:
        model = Translation
        fields = ('id', 'text', 'audio', 'language', 'word')


class FavoriteWordSerializer(serializers.ModelSerializer):
    translation = TranslationSerializer(read_only=True)
    translation_id = serializers.PrimaryKeyRelatedField(
        source='translation',
        queryset=Translation.objects.all(),
        write_only=True
    )

    class Meta:
        model = FavoriteWord
        fields = ('id', 'user', 'translation', 'translation_id')
        read_only_fields = ('user', 'translation')