from rest_framework import serializers
from blog.models import Article
from django.contrib.auth.models import User


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = (
        #     "title",
        #     "slug",
        #     "author",
        #     "content",
        #     "publish",
        #     "status",
        # ) //or
        # exclude = ("created", "updated")
        fields = "__all__"  # all fields


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
