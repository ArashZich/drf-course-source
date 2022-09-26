# from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from blog.models import Article
from .serializers import ArticleSerializer

# Create your views here.


class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
