from django.contrib import admin
from .models import Letter

@admin.register(Letter)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('id', 'letter', 'audio', 'language')
    search_fields = ('letter',)