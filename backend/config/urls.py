from django.contrib import admin
from django.urls import path, include
# from rest_framework.authtoken.views import obtain_auth_token
# from api.views import RevokeToken
from dj_rest_auth.views import PasswordResetConfirmView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("blog.urls")),
    path("api/", include("api.urls")),
    # path('api-auth/', include('rest_framework.urls')),
    # path("api/token-auth/", obtain_auth_token),
    # path("api/revoke/", RevokeToken.as_view()),
    path('api/rest-auth/', include('dj_rest_auth.urls')),
    path('api/rest-auth/registration/',
         include('dj_rest_auth.registration.urls')),
    path('api/rest-auth/password/reset/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(), name='password_reset_confirm'),

]
