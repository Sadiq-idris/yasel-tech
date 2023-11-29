# django core imports
from django.shortcuts import render

# apps imports
from product.models import Product

def home(request):
    products = Product.objects.all()
    context = {
        "title": "Home",
        "products": products[:3],
    }

    return render(request, "index/index.html", context)

def about_us(request):

    context = {
        "title": "About Us"
    }

    return render(request, "index/about_us.html", context)