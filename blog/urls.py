from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from blog import views, blogviews

urlpatterns = [
    path("admin/", admin.site.urls),
    path("Usernamedelete/<str:usernames>",views.Usernamedelete,name="delete"),
    path("UsernamePost/",views.Usernamepost,name="UsernamePost"),
    path("BlogGet/",blogviews.BlogGet,name="BlogGet"),
    path("BlogPost/",blogviews.BlogPost,name="BlogPost"),
    path("Blogdelete/",blogviews.Blogdelete,name="Blogdelete"),
    path("getLogin/",views.getlogin,name="getlogin"),
    path("putlogin/",views.setlogin,name="setlogin"),
    path("generating/",views.generatesomeresp,name="generatesomeresp")
]