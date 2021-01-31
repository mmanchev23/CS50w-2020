from django import forms
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from .models import User, Workout

def index(request):
    return render(request, "apps/index.html")

def about(request):
    return render(request, "apps/about.html")

def tasks(request):
    return render(request, "apps/tasks.html")

def create(request):
    if request.method == "POST":
        name = request.POST["name"]
        content = request.POST["content"]
        workout = Workout(name=name, content=content)
        if workout is not None:
            workout.save()
            return render(request, "apps/create.html", {
                "message": "Workout created successfully!"
            })
        else:
            return render(request, "apps/create.html", {
                "message": "Invalid credentials!"
            })
    else:
        return render(request, "apps/create.html")


def bmi(request):
    return render(request, "apps/bmi.html")

def cc(request):
    return render(request, "apps/cc.html")

def workouts(request):
    workout = Workout.objects.all()
    return render(request, "apps/workouts.html", {
        "workout": workout
    })

def save(request, workoutid):
    workout = Workout.objects.get(pk=workoutid)
    workout.savedInProfile = True
    workout.save()
    return redirect("workouts")

def remove(request, workoutid):
    workout = Workout.objects.get(pk=workoutid)
    workout.savedInProfile = False
    workout.save()
    return redirect("workouts")

def workout(request, workoutid):
    workout = Workout.objects.get(pk=workoutid)
    return render(request, "apps/workout.html", {
        "workout": workout
    })

def edit(request, workoutid):
    if request.method == "POST":
        workout = Workout.objects.get(pk=workoutid)
        newName = request.POST["name"]
        newContent = request.POST["content"]
        workout.name = newName
        workout.content = newContent
        workout.save()
        return render(request, "apps/workout.html", {
            "message": "Workout updated successfully!"
        })
    else:
        return render(request, "apps/workout.html", {
            "message": "Invalid credentials!"
        })


def delete(request, workoutid):
    workout = Workout.objects.get(pk=workoutid)
    workout.delete()
    return redirect("workouts")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "apps/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "apps/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "apps/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "apps/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "apps/register.html")

def profile(request, username):
    workout = Workout.objects.all()
    return render(request, "apps/profile.html", {
        "workout": workout
    })

def config(request, username):
    user = request.user
    if request.method == 'GET':
        profile = User.objects.get(username=username)
        if request.user.is_anonymous:
            return redirect("login")
        if profile.username == user.username:
            return render(request, "apps/config.html", {'profile': profile})
        else:
            return redirect("index")
    else: 
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]

        profile = User.objects.get(username=username)
        profile.first_name = first_name
        profile.last_name = last_name
        email_already = User.objects.filter(email=email)
        if not email_already or profile.email == email:
            profile.email = email
        else:
            return render(request, "apps/config.html", {'profile': profile, 'message': '*Email already taked.'})
        profile.save()
        return redirect('profile', profile.username)