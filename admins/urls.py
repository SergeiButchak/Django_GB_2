from django.urls import path
from admins.views import admins, admin_users_read, admin_users_create, admin_users_update_delete

app_name = 'admins'

urlpatterns = [
    path('', admins, name='admins'),
    path('read/', admin_users_read, name='read'),
    path('create/', admin_users_create, name='create'),
    path('update_delete/', admin_users_update_delete, name='update_delete'),
]
