from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from blog import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("UsernameGet/",views.Usernameget,name="Users"),
    path("Usernamedelete/<str:usernames>",views.Usernamedelete,name="delete"),
    path("UsernamePost/",views.Usernamepost,name="UsernamePost"),
    path("BlogGet/",views.BlogGet,name="BlogGet"),
    path("BlogPost/",views.BlogPost,name="BlogPost"),
    path("Blogdelete/",views.Blogdelete,name="Blogdelete"),
    path("getLogin/",views.getlogin,name="getlogin"),
    path("putlogin/",views.setlogin,name="setlogin"),
    path("generating/",views.generatesomeresp,name="generatesomeresp")
]