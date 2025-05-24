from django.contrib import admin
from .models import Book, Sentence, Category

class SentenceInline(admin.TabularInline):
    model = Sentence
    extra = 0
    can_delete = True

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'language', 'logo')
    search_fields = ('title', 'author')
    inlines = [SentenceInline]

@admin.register(Sentence)
class SentenceAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'audio', 'translate', 'book')
    list_filter = ('book', )
    search_fields = ('text', 'translate')