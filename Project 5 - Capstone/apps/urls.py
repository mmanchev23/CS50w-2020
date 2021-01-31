from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("AboutUs/", views.about, name="about"),
    path("BMICalculator/", views.bmi, name="bmi"),
    path("CalorieCounter/", views.cc, name="cc"),
    path("tasks/", views.tasks, name="tasks"),
    path("workouts/", views.workouts, name="workouts"),
    path("create/", views.create, name="create"),
    path("save/<int:workoutid>", views.save, name="save"),
    path("remove/<int:workoutid>", views.remove, name="remove"),
    path("delete/<int:workoutid>", views.delete, name="delete"),
    path("profile/config/<str:username>", views.config, name="config"),
    path("profile/<str:username>", views.profile, name="profile"),
]