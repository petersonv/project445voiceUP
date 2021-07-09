from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index, name="index"),
    path("home/",views.home, name="home"),
    path("reportit/", views.reportit, name="reportit"),
    path("resources/", views.resources , name="resources"),
    path("help", views.help , name="help"),
    #path("", views. , name="")
]

