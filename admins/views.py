from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse
from users.models import User
from products.models import ProductCategory, Product
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm, CategoryAdminCreateForm, ProductAdminCreateForm


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
            return HttpResponseRedirect(reverse('admins:users_read'))
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


@user_passes_test(lambda u: u.is_staff)
def admin_cat_read(request):
    context = {
        'title': 'GeekShop - Admin',
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'admins/admin-cat-read.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_cat_create(request):
    if request.method == 'POST':
        form = CategoryAdminCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Категория добавлена')
            return HttpResponseRedirect(reverse('admins:cat_read'))
    else:
        form = CategoryAdminCreateForm()
    context = {
        'title': 'Admin - Добавление категории товаров.',
        'form': form
    }
    return render(request, 'admins/admin-cat-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_cat_update(request, pk):
    category = ProductCategory.objects.get(id=pk)
    if request.method == 'POST':
        form = CategoryAdminCreateForm(instance=category, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Измененеия сохранены.')
            return HttpResponseRedirect(reverse('admins:cat_read'))
    else:
        form = CategoryAdminCreateForm(instance=category)
        # print(r.total_quantity)
    context = {
        'title': 'Admin - Изменение категории товара.',
        'form': form,
        'category': category
    }
    return render(request, 'admins/admin-cat-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_cat_delete(request, pk):
    category = ProductCategory.objects.get(id=pk)
    category.delete()
    return HttpResponseRedirect(reverse('admins:cat_read'))


@user_passes_test(lambda u: u.is_staff)
def admin_prod_read(request):
    context = {
        'title': 'GeekShop - Admin',
        'products': Product.objects.all(),
    }
    return render(request, 'admins/admin-prod-read.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_prod_create(request):
    if request.method == 'POST':
        form = ProductAdminCreateForm(data=request.POST)
        if form.is_valid():
            print(form)
            form.save()
            messages.success(request, 'товар добавлен')
            return HttpResponseRedirect(reverse('admins:prod_read'))
        else:
            print(form.errors)

    else:
        form = ProductAdminCreateForm()
    context = {
        'title': 'Admin - Добавление товаров.',
        'form': form
    }
    return render(request, 'admins/admin-prod-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_prod_update(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductAdminCreateForm(instance=product, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Измененеия сохранены.')
            return HttpResponseRedirect(reverse('admins:prod_read'))
    else:
        form = ProductAdminCreateForm(instance=product)
    context = {
        'title': 'Admin - Изменение товара.',
        'form': form,
        'product': product
    }
    return render(request, 'admins/admin-prod-update-delete.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_prod_delete(request, pk):
    product = Product.objects.get(id=pk)
    product.delete()
    return HttpResponseRedirect(reverse('admins:prod_read'))

# Create your views here.
