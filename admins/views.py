from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from users.models import User
from products.models import ProductCategory, Product
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm, CategoryAdminCreateForm, ProductAdminCreateForm


@user_passes_test(lambda u: u.is_staff)
def admins(request):
    context = {'title': 'GeekShop - Admin'}
    return render(request, 'admins/admins.html', context)


class UserListView(ListView):
    model = User
    template_name = 'admins/admin-users-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data()
        context['title'] = 'GeekShop - Admin'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView, self).dispatch(request, args, kwargs)


class UserCreateView(CreateView):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegistrationForm
    success_url = reverse_lazy('admins:users_read')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data()
        context['title'] = 'Admin - Создание пользователя.'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView, self).dispatch(request, args, kwargs)

class UserUpdateView(UpdateView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:users_read')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data()
        context['title'] = 'Admin - Изменение пользователя.'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, args, kwargs)


class UserDeleteView(DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:users_read')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, args, kwargs)


class CategoryListView(ListView):
    model = ProductCategory
    template_name = 'admins/admin-cat-read.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data()
        context['title'] = 'GeekShop - Admin'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryListView, self).dispatch(request, args, kwargs)


class CategoryCreateView(CreateView):
    model = ProductCategory
    template_name = 'admins/admin-cat-create.html'
    form_class = CategoryAdminCreateForm
    success_url = reverse_lazy('admins:cat_read')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data()
        context['title'] = 'Admin - Создание категории.'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryCreateView, self).dispatch(request, args, kwargs)

class CategoryUpdateView(UpdateView):
    model = ProductCategory
    template_name = 'admins/admin-cat-update-delete.html'
    form_class = CategoryAdminCreateForm
    success_url = reverse_lazy('admins:cat_read')
    # fields = ['id', 'name', 'description']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data()
        context['title'] = 'Admin - Изменение категории.'
        return context

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryUpdateView, self).dispatch(request, args, kwargs)


class CategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = 'admins/admin-cat-update-delete.html'
    success_url = reverse_lazy('admins:cat_read')

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryDeleteView, self).dispatch(request, args, kwargs)

# @user_passes_test(lambda u: u.is_staff)
# def admin_users_read(request):
#     context = {
#         'title': 'GeekShop - Admin',
#         'users': User.objects.all(),
#     }
#     return render(request, 'admins/admin-users-read.html', context)


# @user_passes_test(lambda u: u.is_staff)
# def admin_users_create(request):
#     if request.method == 'POST':
#         form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Пользователь создан')
#             return HttpResponseRedirect(reverse('admins:users_read'))
#     else:
#         form = UserAdminRegistrationForm()
#     context = {
#         'title': 'Admin - Создание пользователя.',
#         'form': form
#     }
#     return render(request, 'admins/admin-users-create.html', context)


# @user_passes_test(lambda u: u.is_staff)
# def admin_users_update(request, pk):
#     user = User.objects.get(id=pk)
#     if request.method == 'POST':
#         form = UserAdminProfileForm(instance=user, files=request.FILES, data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Измененеия сохранены.')
#             return HttpResponseRedirect(reverse('admins:users_read'))
#     else:
#         form = UserAdminProfileForm(instance=user)
#         # print(r.total_quantity)
#     context = {
#         'title': 'Admin - Изменение пользователя.',
#         'form': form,
#         'user': user
#     }
#     return render(request, 'admins/admin-users-update-delete.html', context)


# @user_passes_test(lambda u: u.is_staff)
# def admin_users_delete(request, pk):
#     user = User.objects.get(id=pk)
#     user.is_active = False
#     user.save()
#     return HttpResponseRedirect(reverse('admins:users_read'))


# @user_passes_test(lambda u: u.is_staff)
# def admin_cat_read(request):
#     context = {
#         'title': 'GeekShop - Admin',
#         'categories': ProductCategory.objects.all(),
#     }
#     return render(request, 'admins/admin-cat-read.html', context)
#
#
# @user_passes_test(lambda u: u.is_staff)
# def admin_cat_create(request):
#     if request.method == 'POST':
#         form = CategoryAdminCreateForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Категория добавлена')
#             return HttpResponseRedirect(reverse('admins:cat_read'))
#     else:
#         form = CategoryAdminCreateForm()
#     context = {
#         'title': 'Admin - Добавление категории товаров.',
#         'form': form
#     }
#     return render(request, 'admins/admin-cat-create.html', context)
#
#
# @user_passes_test(lambda u: u.is_staff)
# def admin_cat_update(request, pk):
#     category = ProductCategory.objects.get(id=pk)
#     if request.method == 'POST':
#         form = CategoryAdminCreateForm(instance=category, data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Измененеия сохранены.')
#             return HttpResponseRedirect(reverse('admins:cat_read'))
#     else:
#         form = CategoryAdminCreateForm(instance=category)
#         # print(r.total_quantity)
#     context = {
#         'title': 'Admin - Изменение категории товара.',
#         'form': form,
#         'category': category
#     }
#     return render(request, 'admins/admin-cat-update-delete.html', context)
#
#
# @user_passes_test(lambda u: u.is_staff)
# def admin_cat_delete(request, pk):
#     category = ProductCategory.objects.get(id=pk)
#     category.delete()
#     return HttpResponseRedirect(reverse('admins:cat_read'))


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
