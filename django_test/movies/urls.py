from django.urls import path, include # imports the path function
from . import views # import the view function we made in de views.py

urlpatterns = [ # add de pages from webserver to a list
path("", views.index, name="index"),
path("info", views.info, name="info"),
# path("input/", include("movies.urlsecond")),
path("input/<int:id>", views.get_id, name="get_id"),
path("makeReview", views.makeReview, name="make_review"),
#path("subpath", views.info, name="info"), # sub path 

]