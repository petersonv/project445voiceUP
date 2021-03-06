from django.shortcuts import render, redirect
#from django.contrib.auth import login, authenticate
#from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages



# register function validates the form, if not an empty form is shown
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        #alert for successful login
        messages.success(response, "You have logged in successfully!")
        return redirect("/home")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})