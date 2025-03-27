from rest_framework import serializers
from .models import Book, Sentence, CompletedBook, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    language = serializers.StringRelatedField()
    category = CategorySerializer()

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'category', 'language', 'logo')


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