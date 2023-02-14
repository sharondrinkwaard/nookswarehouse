from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from products.models import Product


def overview_orders(request):
    """ A view to display the orders made by the authenticated customer """
    return render(request, 'shoppingcart/overview_orders.html')


def add_to_cart(request, article_id):
    """ A view to add articles to the shopping cart """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    if 'size_option' in request.POST:
        size = request.POST['size_option']
    cart = request.session.get('cart', {})

    if size:
        if article_id in list(cart.keys()):
            if size in cart[article_id]['items_by_size'].keys():
                cart[article_id]['items_by_size'][size] += quantity
            else:
                cart[article_id]['items_by_size'][size] = quantity
        else:
            cart[article_id] = {'items_by_size': {size: quantity}}

    else:
        if article_id in list(cart.keys()):
            cart[article_id] += quantity
        else:
            cart[article_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)


def edit_cart(request, article_id):
    """ Change the quantity and / or size of the product """

    product = get_object_or_404(Product, pk=article_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    print("In the view")

    if 'size_option' in request.POST:
        size = request.POST['size_option']
        print('SIZE OPTION IS: ', size)
    cart = request.session.get('cart', {})

    if size:
        print('THE SIZE IS: ', size)
        if quantity > 0:
            print('Size exists and quantity is > 0')
            cart[article_id]['items_by_size'][size] = quantity
            print(quantity)
            # messages.success(request, f'Updated size {size.upper()} {product.name} quantity to {bag[item_id]["items_by_size"][size]}')
        else:
            del cart[article_id]['items_by_size'][size]
            if not cart[article_id]['items_by_size']:
                cart.pop(article_id)
            # messages.success(request, f'Removed size {size.upper()} {product.name} from your bag')
    else:
        if quantity > 0:
            cart[article_id] = quantity
            # messages.success(request, f'Updated {product.name} quantity to {bag[article_id]}')
        else:
            cart.pop(article_id)
            # messages.success(request, f'Removed {product.name} from your bag')

    request.session['cart'] = cart
    return redirect(reverse('overview_orders'))


def delete_from_cart(request, article_id):
    """ Delete article from shopping cart """

    product = get_object_or_404(Product, pk=article_id)
    size = None
    if 'size_option' in request.POST:
        size = request.POST['size_option']
    cart = request.session.get('cart', {})

    if size:
        del cart[article_id]['items_by_size'][size]
        if not cart[article_id]['items_by_size']:
            cart.pop(article_id)
        # messages.success(request, f'Removed size {size.upper()} {product.name} from your cart')
    else:
        cart.pop(article_id)
        # messages.success(request, f'Removed {product.name} from your cart')

    request.session['cart'] = cart
    return HttpResponse(status=200)
