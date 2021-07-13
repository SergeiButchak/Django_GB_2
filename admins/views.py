from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from users.models import User
from admins.forms import UserAdminRegistrationForm

def admins(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/admins.html', context)


def admin_users_read(request):
    context = {
        'title': 'GeekShop - Admin',
        'users': User.objects.all(),
    }
    return render(request, 'admins/admin-users-read.html', context)


def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь создан')
            return HttpResponseRedirect(reverse('admins:create'))
    else:
        form = UserAdminRegistrationForm()
    context = {
        'title': 'Admin - Создание пользователя.',
        'form': form
    }
    return render(request, 'admins/admin-users-create.html', context)


def admin_users_update_delete(request, id):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/admin-users-update-delete.html', context)
# Create your views here.
