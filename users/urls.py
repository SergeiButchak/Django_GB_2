from django.urls import path

from users.views import login, registration, logout

app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='register'),
    path('logout/', logout, name='logout'),
]