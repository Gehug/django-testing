from http.client import HTTPResponse
from django.shortcuts import render

from django.contrib.auth import login, authenticate
from .forms import CreateAccount

# Create your views here.


def create(response):
    if response.method == "POST":
        form = CreateAccount(response.POST)
        if form.is_valid():
            form.save()

    else:
        form = CreateAccount()

    return render(response, "register/createAccount.html", {"form":form})

def login(response):
    form = CreateAccount()
    return render(response, "register/createAccount.html", {"form":form})

def logout(response):
    return render(response, "register/logout.html")

