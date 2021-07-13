from django.urls import path
from admins.views import admins, admin_users_read, admin_users_create, admin_users_update, admin_users_delete

app_name = 'admins'

urlpatterns = [
    path('', admins, name='admins'),
    path('users/read/', admin_users_read, name='users_read'),
    path('users/create/', admin_users_create, name='users_create'),
    path('users/update/<int:pk>/', admin_users_update, name='users_update'),
    path('users/delete/<int:pk>/', admin_users_delete, name='users_delete'),
]
