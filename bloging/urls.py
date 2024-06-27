from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from blog import views,urls
import rest_framework_simplejwt.views as v
from rest_framework.authtoken import views
# print(help(v))
# from rest_framework_simplejwt.views import TokenObtainpairView


urlpatterns=[
    path("blog/",include(urls)),
    path('api-token-auth/', views.obtain_auth_token)

]