from rest_framework import serializers
from blog.models import Article
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from drf_dynamic_fields import DynamicFieldsMixin

# class AuthorUsernameField(serializers.RelatedField):
#     def to_representation(self, value):
#         return value.username

class ArticleSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    # author = AuthorUsernameField(read_only=True)
    # author = serializers.CharField(source="author.username",read_only=True)
    def get_author(self,obj):
        return {
            "username":obj.author.username,
            "first_name":obj.author.first_name,
            "last_name":obj.author.last_name,

        }
    author = serializers.SerializerMethodField("get_author")


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

    def validate_title(self, value):
        filter_list = ["javascript", "laravel", "PHP"]
        for i in filter_list:
            if i in value:
                raise serializers.ValidationError(
                    "Don't use bad world!: {}".format(i))


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        # model = User
        model = get_user_model()
        fields = "__all__"
