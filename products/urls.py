from django.urls import path

from products.views import products

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('category/<int:category_id>/', products, name='categories'),
    path('page/<int:page>/', products, name='page'),
    path('category/<int:category_id>/page/<int:page>/', products, name='cat_page'),
]