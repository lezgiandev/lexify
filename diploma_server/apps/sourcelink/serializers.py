from rest_framework import serializers
from .models import Category, Source, MarkedSource

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SourceSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    language = serializers.StringRelatedField()

    class Meta:
        model = Source
        fields = ('id', 'text', 'link', 'language', 'category')


class MarkedSourceSerializer(serializers.ModelSerializer):
    source = SourceSerializer(read_only=True)
    source_id = serializers.PrimaryKeyRelatedField(
        source='source',
        queryset=Source.objects.all(),
        write_only=True
    )

    class Meta:
        model = MarkedSource
        fields = ('id', 'user', 'source', 'source_id')
        read_only_fields = ('user', 'source')