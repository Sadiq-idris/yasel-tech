# django core imports
from django.shortcuts import render, get_object_or_404

# apps imports
from .models import Product

def product(request):

    computers = Product.objects.filter(tags="computer")
    iwatchs = Product.objects.filter(tags="iwatch")
    airpods = Product.objects.filter(tags="airpod")

    context = {
        "title": "Product",
        "computers":computers,
        "iwatchs":iwatchs,
        "airpods":airpods,
    }

    return render(request, "product/product.html", context)


def detail(request, pk):
    product = get_object_or_404(Product, id=pk)
    context = {
        "title": "Product",
        "product":product,
    }

    return render(request, "product/detail.html", context)