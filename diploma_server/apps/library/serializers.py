from rest_framework import serializers
from .models import Book, Sentence, CompletedBook


class BookSerializer(serializers.ModelSerializer):
    language = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'language', 'logo')


class SentenceSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = Sentence
        fields = ('id', 'text', 'audio', 'translate', 'book')


class CompletedBookSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    book_id = serializers.PrimaryKeyRelatedField(
        source='book',
        queryset=Book.objects.all(),
        write_only=True
    )

    class Meta:
        model = CompletedBook
        fields = ('id', 'user', 'book', 'book_id')
        read_only_fields = ('user', 'book')