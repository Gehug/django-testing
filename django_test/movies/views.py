from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User

from .models import Movie, Review
from .forms import review_form

import json



# Create your views here.
def index(response): # View movies reviews
    all_movies = Movie.objects.all()

    return render(response, "movies/index.html", {"title":"home", "all_movies": all_movies})

def makeReview(response):

    MakeReviewForms = review_form() # gaat elke keer de form class terug aanmaken, voor het dynamisch effect te krijgen wanneer er een veld update (komt film bij of er gaat film af)


    if response.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MakeReviewForms(response.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
        
            movie_name = form.cleaned_data["movieName"]
            review = form.cleaned_data["review"]
            
            u = response.user
            movie_obj = Movie.objects.get(name__iexact=movie_name)
            Review.objects.create(movie=movie_obj, username=u, review=review, stars=2)
  
            return HttpResponseRedirect('/testing/')

    else:
        
        form = MakeReviewForms()


    return render(response, 'movies/makeReview.html', {'form': form})


def info(response): # Add movie review

    return HttpResponse("just some info")




# def input(response):
#     m = MovieList(name="All movies")
#     m.save()
# # m.movie_set.create(title="Titanic", description="Grote boot dat zinkt", picture="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-oUFRn_Err2mBTIRXR0FEuTbjJXS687eoCXHBAVBZ-v8xyeJw")
#     m.movie_set.all(id=id)
# # <QuerySet [<Movie: Titanic>]>
#     return HttpResponse()




def get_id(response, id):
    # m = MovieList(name="All movies")
    # m.save()
    # m.movie_set.create(title="Titanic", description="Grote boot dat zinkt", picture="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT-oUFRn_Err2mBTIRXR0FEuTbjJXS687eoCXHBAVBZ-v8xyeJw")
    item = Movie.objects.get(id=id)
    #item = m.movie_set.all()
    return HttpResponse(item)



# Login django admin
# username: gil
# password: 123