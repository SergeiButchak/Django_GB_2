from django.shortcuts import render
from django.core import serializers
from products.models import Product
import json
# Create your views here.


def index(request):
    context = {
        "title": "GeekShop",
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        "title": "GeekShop - Каталог",
    }
    context['products'] = Product.objects.all()
    return render(request, 'products/products.html', context)
