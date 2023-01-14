from products.models import Product
from django.shortcuts import get_object_or_404
from django.conf import settings


def shopping_content(request):

    shopping_items = []
    total = 0
    product_count = 0
    delivery = 0
    cart = request.session.get('cart', {})
    # delete before deployment
    print(cart)

    for article_id, item_data in cart.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=article_id)
            total += item_data * product.price
            product_count += item_data
            shopping_items.append({
                'article_id': article_id,
                'quantity': item_data,
                'product': product,
            })
        else:
            product = get_object_or_404(Product, pk=article_id)
            for size, quantity in item_data['items_by_size'].items():
                total += quantity * product.price
                product_count += quantity
                shopping_items.append({
                    'article_id': article_id,
                    'quantity': quantity,
                    'product': product,
                    'size': size,
                })
    # Grand total is not in use yet
    # Note: I will need it when continuing after submitting PP5.
    grand_total = total + delivery

    context = {
        'shopping_items': shopping_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
