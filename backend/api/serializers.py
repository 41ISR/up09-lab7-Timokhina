from rest_framework import serializers
from .models import Article

from rest_framework import serializers
from .models import Article

class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title', 'desc', 'tags', 'created_at', 'author', 'image']

class ArticleViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'