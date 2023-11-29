# django core imports 
from django.urls import path

# apps imports
from . import views


urlpatterns = [
    path("", views.product, name="product"),
    path("detail/<int:pk>", views.detail, name="detail"),
]