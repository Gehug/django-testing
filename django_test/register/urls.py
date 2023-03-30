from django.urls import path, include 
from . import views

urlpatterns = [ # add de pages from webserver to a list
path("", views.create, name="create"),
path("create-account", views.create, name="create"),
path("login", views.login, name="login"),
path("logout", views.logout, name="logout"),
]