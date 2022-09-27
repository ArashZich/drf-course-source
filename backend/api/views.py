# from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsSuperUserOrStaffReadOnly, IsAuthorOrReadOnly, IsStaffOrReadOnly
from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer
from django.contrib.auth.models import User


# Create your views here.

# ListCreateAPIView ==> all data
# RetrieveAPIView ==> get by id
# DestroyAPIView ==> delete
# RetrieveDestroyAPIView ==> delete and get
# UpdateAPIView ==> update
# RetrieveUpdateAPIView ==> update and get
# RetrieveUpdateDestroyAPIView ==> update, delete and get


class ArticleList(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)


class ArticleGet(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDelete(DestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)


class ArticleUpdate(UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsStaffOrReadOnly, IsAuthorOrReadOnly)


class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = {IsSuperUserOrStaffReadOnly, }


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = {IsSuperUserOrStaffReadOnly, }


class UserGet(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = {IsSuperUserOrStaffReadOnly, }


class UserDelete(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = {IsSuperUserOrStaffReadOnly, }


class UserUpdate(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = {IsSuperUserOrStaffReadOnly, }
