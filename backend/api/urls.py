from rest_framework import routers
from django.urls import path, include
# from .views import ArticleList, ArticleDetail, ArticleGet, ArticleDelete, ArticleUpdate, UserList, UserDetail, UserGet, UserDelete, UserUpdate
from .views import UserViewSet, ArticleViewSet
app_name = "api"

# urlpatterns = [
#     path("", ArticleList.as_view(), name='list'),
#     path("<int:pk>", ArticleDetail.as_view(), name='detail'),
#     path("<int:pk>/get", ArticleGet.as_view(), name='detail_get'),
#     path("<int:pk>/delete", ArticleDelete.as_view(), name='detail_delete'),
#     path("<int:pk>/update", ArticleUpdate.as_view(), name='detail_update'),
#     # //user
#     path("users/", UserList.as_view(), name='user-list'),
#     path("users/<int:pk>", UserDetail.as_view(), name='user-detail'),
#     path("users/<int:pk>/get", UserGet.as_view(), name='user-detail'),
#     path("users/<int:pk>/delete", UserDelete.as_view(), name='user-detail'),
#     path("users/<int:pk>/update", UserUpdate.as_view(), name='user-detail'),
# ]

router = routers.SimpleRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('users', UserViewSet, basename='users')

# urlpatterns = router.urls
# or
urlpatterns = [
    path("", include(router.urls)),
]
