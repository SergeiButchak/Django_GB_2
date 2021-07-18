from django.shortcuts import render
from django.core import serializers
from products.models import Product, ProductCategory
import json
# Create your views here.


def index(request):
    context = {
        "title": "GeekShop",
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None):
    context = {
        "title": "GeekShop - Каталог",
        "categories": ProductCategory.objects.all()
    }
    if category_id:
        context['products'] = Product.objects.filter(category=category_id)
    else:
        context['products'] = Product.objects.all()

    return render(request, 'products/products.html', context)
