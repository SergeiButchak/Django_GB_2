from django.urls import path
from admins.views import admins, UserListView, UserCreateView, UserUpdateView, UserDeleteView
from admins.views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView
from admins.views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView

app_name = 'admins'

urlpatterns = [
    path('', admins, name='admins'),
    path('users/read/', UserListView.as_view(), name='users_read'),
    path('users/create/', UserCreateView.as_view(), name='users_create'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='users_update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='users_delete'),
    path('cat/read/', CategoryListView.as_view(), name='cat_read'),
    path('cat/create/', CategoryCreateView.as_view(), name='cat_create'),
    path('cat/update/<int:pk>/', CategoryUpdateView.as_view(), name='cat_update'),
    path('cat/delete/<int:pk>/', CategoryDeleteView.as_view(), name='cat_delete'),
    path('prod/read/', ProductListView.as_view(), name='prod_read'),
    path('prod/create/', ProductCreateView.as_view(), name='prod_create'),
    path('prod/update/<int:pk>/', ProductUpdateView.as_view(), name='prod_update'),
    path('prod/delete/<int:pk>/', ProductDeleteView.as_view(), name='prod_delete'),

]
