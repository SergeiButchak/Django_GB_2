from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from products.models import Product, ProductCategory
import json
# Create your views here.


def index(request):
    context = {
        "title": "GeekShop",
    }
    return render(request, 'products/index.html', context)


# def products(request, category_id=None, page=1):
#     context = {
#         "title": "GeekShop - Каталог",
#         "categories": ProductCategory.objects.all(),
#         "current_cat": category_id,
#     }
#     if category_id:
#         products = Product.objects.filter(category=category_id)
#     else:
#         products = Product.objects.all()
#     paginator = Paginator(products, 3)
#     try:
#         products_paginator = paginator.page(page)
#     except PageNotAnInteger:
#         products_paginator = paginator.page(1)
#     except EmptyPage:
#         products_paginator = paginator.page(paginator.num_pages)
#     context['products'] = products_paginator
#     return render(request, 'products/products.html', context)


class ProductListView(ListView):
    model = Product
    paginate_by = 3
    template_name = 'products/products.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        filter_cat = self.kwargs.get('category_id', None)
        if filter_cat:
            self.set_category_filter(filter_cat)
        context = super(ProductListView, self).get_context_data()
        context['title'] = 'GeekShop - Каталог'
        context['categories'] = ProductCategory.objects.all()
        context['filter'] = filter_cat
        return context

    def set_category_filter(self, filter_cat):
        self.object_list = Product.objects.filter(category=filter_cat)
