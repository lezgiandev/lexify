from django.contrib import admin
from .models import Category, Word, Translation, PartOfSpeech


class TranslationInline(admin.TabularInline):
    model = Translation
    extra = 0
    can_delete = True

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(PartOfSpeech)
class PartOfSpeechAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', )


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'part_of_speech', 'category')
    list_filter = ('category',)
    search_fields = ('text',)
    inlines = [TranslationInline]

@admin.register(Translation)
class TranslationAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'language', 'text', 'audio')
    list_filter = ('language',)
    search_fields = ('text', 'word__text')