from django.conf import settings
from django.db import models



# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="movie_cover_pictures/")

        
    def __str__(self):
        return self.name


class Review(models.Model):

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE) # SQL kind of things
    username = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    review = models.CharField(max_length=200)
    stars = models.SmallIntegerField()

    def __str__(self):
        return self.review

        






# from models import MovieList, Movie
# m = MovieList("All movies")
# m.movie_set.create(title="Titanic", description="Grote boot dat zinkt", picture="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-oUFRn_Err2mBTIRXR0FEuTbjJXS687eoCXHBAVBZ-v8xyeJw")
# m.movie_set.all()
# <QuerySet [<Movie: Titanic>]>

