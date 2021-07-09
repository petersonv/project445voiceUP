from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("<h1>First View</h1>")

def home(response):
    return HttpResponse("<h1>Home Page</h1>")

def reportit(response):
    return HttpResponse("<h1>Report It Page</h1>")

def resources(response):
    return HttpResponse("<h1>Resources Page</h1>")

def help(response):
    return HttpResponse("<h1>Help Page</h1>")