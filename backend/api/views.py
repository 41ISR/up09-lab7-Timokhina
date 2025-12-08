from django.shortcuts import render
from rest_framework import viewsets
from .models import Article
from .serializers import ArticleListSerializer

class ArticleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Article.objects.all().order_by("-created_at")

    def get_serializer_class(self):
        if self.action == "retrieve":
            return ArticleListSerializer
        return ArticleListSerializer