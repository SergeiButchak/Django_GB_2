from django.db import models
from django.db.models import Sum, F
from users.models import User
from products.models import Product
# Create your models here.

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.products.name}'

    def sum(self):
        return self.quantity * self.products.price

    def total_quantity(self):
        return Basket.objects.filter(user=self.user).aggregate(total=Sum('quantity')).get('total')

    def total_sum(self):
        return Basket.objects.filter(user=self.user).aggregate(sum=Sum(F('quantity')*F('products__price'))).get('sum')