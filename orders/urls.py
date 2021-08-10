from django.urls import path
from orders import views


app_name = 'orders'


urlpatterns = [
    path('', views.OrderListView.as_view(), name='orders_list'),
    path('create/', views.OrderCreateView.as_view(), name='order_create'),
    path('read/<pk>/', views.OrderDetailView.as_view(), name='order_read'),
    path('update/<pk>/', views.OrderUpdateView.as_view(), name='order_update'),
    path('delete/<pk>/', views.OrderDeleteView.as_view(), name='order_delete'),
    path('forming/complete/<pk>', views.order_forming_complete, name='order_forming_complete'),
]