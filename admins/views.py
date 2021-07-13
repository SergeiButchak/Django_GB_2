from django.shortcuts import render


def admins(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/admins.html', context)


def admin_users_read(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/admin-users-read.html', context)


def admin_users_create(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/admin-users-create.html', context)


def admin_users_update_delete(request, id):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/admin-users-update-delete.html', context)
# Create your views here.
