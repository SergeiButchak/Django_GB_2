from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from django.conf import settings
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from baskets.models import Basket
# Create your views here.


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'title': 'GeekShop - Авторизация',
        'form': form,
    }
    return render(request, 'users/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if send_verify_mail(user):
                print('Success sending mail')
            else:
                print('Sending mail failed')
            messages.success(request, 'Вы успешно зарегистрированы.')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {
        'title': 'GeekShop - Регистрация',
        'form': form
    }
    return render(request, 'users/register.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, files=request.FILES, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Измененеия сохранены.')
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
        r = Basket.objects.filter(user=request.user)
        # print(r.total_quantity)
    context = {
        'title': 'GeekShop - Личный кабинет',
        'form': form,
        'baskets': Basket.objects.filter(user=request.user),
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


def verify(request, email, activation_key):
    pass


def send_verify_mail(user):
    subject = 'Verify your account'
    link = reverse('users:verify', args=[user.email, user.activation_key])
    message = f'{settings.DOMAIN}{link}'
    return send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
