from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return render(response, "main/base.html", {})

def home(response):
    return render(response, "main/home.html", {})

def reportit(response):
    return render(response, "main/reportit.html", {})

def resources(response):
    return render(response, "main/resources.html", {})

def help(response):
    return render(response, "main/help.html", {})