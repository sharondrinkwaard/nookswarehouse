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
        'stripe_public_key': 'pk_test_51McQpqGL29wYvReMN5NRcKhCFIuOHM7YVGCyeaPx9ylJIKcwerMaSeEw56Ww8aQfTeWobAedsQguQzNQGku1iDGn00X6cduK9s',
        'client_secret': 'test client secret'
    }
    return render(request, template, context)
