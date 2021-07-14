from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm


@user_passes_test(lambda u: u.is_staff)
def admins(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/admins.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_read(request):
    context = {
        'title': 'GeekShop - Admin',
        'users': User.objects.all(),
    }
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пользователь создан')
            return HttpResponseRedirect(reverse('admins:read'))
    else:
        form = UserAdminRegistrationForm()
    context = {
        'title': 'Admin - Создание пользователя.',
        'form': form
    }
    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_update(request, pk):
    user = User.objects.get(id=pk)
    if request.method == 'POST':
        form = UserAdminProfileForm(instance=user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Измененеия сохранены.')
            return HttpResponseRedirect(reverse('admins:users_read'))
    else:
        form = UserAdminProfileForm(instance=user)
        # print(r.total_quantity)
    context = {
        'title': 'Admin - Изменение пользователя.',
        'form': form,
        'user': user
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_users_delete(request, pk):
    user = User.objects.get(id=pk)
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admins:users_read'))
# Create your views here.
