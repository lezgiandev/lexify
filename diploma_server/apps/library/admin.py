from django.contrib import admin
from .models import Book, Sentence


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'language', 'logo')
    search_fields = ('title', 'author')


@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'audio', 'translate', 'book')
    list_filter = ('book', )
    search_fields = ('text', 'translate')