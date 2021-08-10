from django.db import transaction
from django.forms import inlineformset_factory
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from baskets.models import Basket
from orders.forms import OrderItemForm
from orders.models import Order, OrderItem


class OrderListView(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderDetailView(DetailView):
    model = Order
    extra_context = {'title': 'Geekshop - просмотр заказа'}


class OrderUpdateView(UpdateView):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:orders_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)
        formset = OrderFormSet(instance=self.object)

        if self.request.method == 'POST':
            formset = OrderFormSet(self.request.POST, instance=self.object)

        context.update({
            'title': 'Geekshop: редактирование заказа',
            'orderitems': formset
        })

        return context

    def form_valid(self, form):
        orderitems = self.get_context_data()['orderitems']
        form.instance.user = self.request.user
        self.object = form.save()

        if orderitems.is_valid():
            orderitems.instance = self.object
            orderitems.save()

        return super().form_valid(form)


class OrderDeleteView(DeleteView):
    model = Order
    success_url = reverse_lazy('orders:orders_list')


class OrderCreateView(CreateView):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:orders_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=1)
        formset = OrderFormSet()

        if self.request.method == 'POST':
            formset = OrderFormSet(self.request.POST)
        else:
            basket_items = Basket.objects.filter(user_id=self.request.user.id)
            if basket_items.exists():
                OrderFormSet = inlineformset_factory(Order, OrderItem, form=OrderItemForm, extra=basket_items.count())
                formset = OrderFormSet()
                for num, form in enumerate(formset.forms):
                    form.initial['product'] = basket_items[num].products
                    form.initial['quantity'] = basket_items[num].quantity

        context.update({
            'title': 'Geekshop: создание заказа',
            'orderitems': formset
        })

        return context

    def form_valid(self, form):
        orderitems = self.get_context_data()['orderitems']
        basket_items = Basket.objects.filter(user=self.request.user)

        with transaction.atomic():
            form.instance.user = self.request.user
            self.object = form.save()

            if orderitems.is_valid():
                orderitems.instance = self.object
                orderitems.save()
                basket_items.delete()

        return super().form_valid(form)


def order_forming_complete(request, pk):
    order_item = get_object_or_404(Order, pk=pk)
    order_item.status = Order.SENT_TO_PROCEED
    order_item.save()
    return HttpResponseRedirect(reverse('orders:order_read', args=[order_item.pk]))