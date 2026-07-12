from django.shortcuts import render,redirect
from .models import Register
from django.contrib.auth import authenticate, login, logout

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        name = request.POST.get("name")
        age = request.POST.get("age")

        Register.objects.create_user(
            username=username,
            password=password,
            name=name,
            age=age
        )

        return redirect("signin")

    return render(request, "signup.html")

def signin(request):
    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("home")

    return render(request, "signin.html")

def signout(request):
    logout(request)
    return redirect("signin")