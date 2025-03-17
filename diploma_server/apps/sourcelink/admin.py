from django.contrib import admin
from .models import Source, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'link', 'language', 'category')
    search_fields = ('text',)