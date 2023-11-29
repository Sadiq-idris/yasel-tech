# django core imports
from django.urls import path

# apps imports
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about-us/", views.about_us, name="about_us"),
]