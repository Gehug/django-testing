from django import forms
from .models import Movie





def review_form():
	class MakeReviewForms(forms.Form):
		movie_list = []
		for movie in Movie.objects.all():
			movie_list.append((movie.name, movie.name))
		movieName = forms.CharField(label="Movie Name",widget=forms.Select(choices=movie_list),max_length=100)
		review = forms.CharField(label="Review",max_length=500)
	return MakeReviewForms


