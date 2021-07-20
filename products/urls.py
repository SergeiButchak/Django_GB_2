from django.urls import path

from products.views import ProductListView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('category/<int:category_id>/', ProductListView.as_view(), name='categories'),
    path('page/<int:page>/', ProductListView.as_view(), name='page'),
    path('category/<int:category_id>/page/<int:page>/', ProductListView.as_view(), name='cat_page'),
    # path('category/<int:category_id>/', products, name='categories'),
    # path('page/<int:page>/', products, name='page'),
    # path('category/<int:category_id>/page/<int:page>/', products, name='cat_page'),
]