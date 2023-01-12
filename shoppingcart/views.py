from django.shortcuts import render, redirect


def overview_orders(request):
    """ A view to display the orders made by the authenticated customer """
    return render(request, 'shoppingcart/overview_orders.html')


def add_to_cart(request, article_id):
    """ A view to add articles to the shopping cart """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    # if 'product_size' in request.POST:
    #     size = request.POST['size']
    cart = request.session.get('cart', {})

    # if size:
    #     if article_id in list(cart.keys()):

    if article_id in list(cart.keys()):
        cart[article_id] += quantity
    else:
        cart[article_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)
