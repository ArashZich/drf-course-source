# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
# from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.permissions import IsAuthenticated
from .permissions import IsSuperUserOrStaffReadOnly, IsAuthorOrReadOnly, IsStaffOrReadOnly
from blog.models import Article
from .serializers import ArticleSerializer, UserSerializer
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model


# Create your views here.

# ListCreateAPIView ==> all data
# RetrieveAPIView ==> get by id
# DestroyAPIView ==> delete
# RetrieveDestroyAPIView ==> delete and get
# UpdateAPIView ==> update
# RetrieveUpdateAPIView ==> update and get
# RetrieveUpdateDestroyAPIView ==> update, delete and get

# Article

"""

old: many view

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

"""

# new: Model View Set


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    filterset_fields = ["status", "author"]
    # filterset_fields = ["status", "author__username"]
    search_fields = ["title", "content", "author__username",
                     "author__first_name", "author__last_name"]
    ordering_fields = ["publish", "status"]
    ordering = ["-publish"]

    # old filter
    # def get_queryset(self):
    #     queryset = Article.objects.all()
    #     status = self.request.query_params.get('status')
    #     if status is not None:
    #         queryset = queryset.filter(status=status)

    #     author = self.request.query_params.get('author')
    #     if author is not None:
    #         queryset = queryset.filter(author__username=author)

    #     return queryset

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly, IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


# User Api

"""

old: many view

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

"""

# new: Model View Set


class UserViewSet(ModelViewSet):
    # queryset = User.objects.all()
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = {IsSuperUserOrStaffReadOnly, }


# class RevokeToken(APIView):
#     permission_classes = (IsAuthenticated,)

#     def delete(self, request):
#         request.auth.delete()
#         return Response(status=204)

