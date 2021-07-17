from django.urls import path
from admins.views import admins, admin_users_read, admin_users_create, admin_users_update, admin_users_delete
from admins.views import admin_cat_read, admin_cat_create, admin_cat_update, admin_cat_delete
from admins.views import admin_prod_read, admin_prod_create, admin_prod_update, admin_prod_delete

app_name = 'admins'

urlpatterns = [
    path('', admins, name='admins'),
    path('users/read/', admin_users_read, name='users_read'),
    path('users/create/', admin_users_create, name='users_create'),
    path('users/update/<int:pk>/', admin_users_update, name='users_update'),
    path('users/delete/<int:pk>/', admin_users_delete, name='users_delete'),
    path('cat/read/', admin_cat_read, name='cat_read'),
    path('cat/create/', admin_cat_create, name='cat_create'),
    path('cat/update/<int:pk>/', admin_cat_update, name='cat_update'),
    path('cat/delete/<int:pk>/', admin_cat_delete, name='cat_delete'),
    path('prod/read/', admin_prod_read, name='prod_read'),
    path('prod/create/', admin_prod_create, name='prod_create'),
    path('prod/update/<int:pk>/', admin_prod_update, name='prod_update'),
    path('prod/delete/<int:pk>/', admin_prod_delete, name='prod_delete'),

]
