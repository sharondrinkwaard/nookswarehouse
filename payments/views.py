from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def payments(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, 'There is nothing in your shoppingcart.')
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'payments/payments.html'
    context = {
        'order_form': order_form,
    }
    return render(request, template, context)
