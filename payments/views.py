from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import OrderForm
from shoppingcart.contexts import shopping_content
from .models import OrderLineItem, Order
from products.models import Product
import stripe


def payments(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})

        payment_form_data = {
            'first_name': request.POST['first_name'],
            'last_name': request.POST['last_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'city': request.POST['city'],
            'street_address': request.POST['street_address'],
            'house_number': request.POST['house_number'],
            'county': request.POST['county'],
            'country': request.POST['country'],
        }

        order_form = OrderForm(payment_form_data)
        if order_form.is_valid():
            # order = order_form.save(commit=False)
            # pid = request.POST.get('client_secret').split('_secret')[0]
            # order.stripe_pid = pid
            # order.original_bag = json.dumps(bag)
            order = order_form.save()
            for article_id, item_data in cart.items():
                try:
                    product = Product.objects.get(id=article_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
                except Product.DoesNotExist:
                    print('Product in cart does not exist.')
                    # messages.error(request, (
                    #     "One of the products in your cart wasn't found in our database. "
                    #     "Please call us for assistance!")
                    # )
                    order.delete()
                    return redirect(reverse('overview_orders'))

            # Save the info to the user's profile
            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('payment_succes', args=[order.order_number]))
        else:
            print('Error in the form')
            # messages.error(request, 'There was an error with your form. \
            #     Please double check your information.')
    else:
        cart = request.session.get('cart', {})
        if not cart:
            # messages.error(request, "There's nothing in your cart at the moment")
            print('Shopping cart empty')
            return redirect(reverse('products'))

    current_cart = shopping_content(request)
    total = current_cart['grand_total']
    order_form = OrderForm()
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

# Attempt to prefill the form with any info the user maintains in their profile
# if request.user.is_authenticated:
#     try:
#         profile = UserProfile.objects.get(user=request.user)
#         order_form = OrderForm(initial={
#             'first_name': request.POST['first_name'],
#             'last_name': request.POST['last_name'],
#             'email': request.POST['email'],
#             'phone_number': request.POST['phone_number'],
#             'postcode': request.POST['postcode'],
#             'city': request.POST['city'],
#             'street_address': request.POST['street_address'],
#             'house_number': request.POST['house_number'],
#             'county': request.POST['county'],
#             'country': request.POST['country'],
#         })
#     except UserProfile.DoesNotExist:
#         order_form = OrderForm()
# else:
#     order_form = OrderForm()

    if not stripe_public_key:
        print('Stripe key missing')
        # messages.warning(request, 'Stripe public key is missing. \
        #     Did you forget to set it in your environment?')

    template = 'payments/payments.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def payment_succes(request, order_number):
    ''' Handles succesful payments'''
    save_info = request.session.get('save-info')
    order = get_object_or_404(Order, order_number=order_number)
    # messages.succes(request, f'Order placed succesfully! \
        # Your order number is {order_number}. \
        # A confirmation email will be send to {order.email} ')

    if 'cart' in request.session:
        del request.session['cart']

    template = 'payments/payment_succes.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
