from audioop import maxpp
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User






class CreateAccount(UserCreationForm):

	email = forms.EmailField()
	firstname = forms.CharField(label="firstname", max_length=100)
	lastname = forms.CharField(label="lastname", max_length=100)



	class Meta():
		model = User
		fields = ["username", "email", "firstname", "lastname", "password1", "password2"]


# 	first_name = forms.CharField(label="First name",max_length=100)
# 	last_name = forms.CharField(label="Last Name",max_length=100)
# 	email = forms.CharField(label="email",max_length=100)
# 	password1 = forms.PasswordInput(label="password1",max_length=100)
# 	password2 = forms.PasswordInput(label="password2",max_length=100)





