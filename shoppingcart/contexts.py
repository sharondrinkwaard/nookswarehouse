from products.models import Product
from django.shortcuts import get_object_or_404
from django.conf import settings


def shopping_content(request):

    shopping_items = []
    total = 0
    product_count = 0
    delivery = 0
    cart = request.session.get('cart', {})

    for article_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=article_id)
        # q_s = get_object_or_404(QuantitySize, pk=qs_id)
        total += quantity * product.price
        product_count += quantity
        shopping_items.append({
            'article_id': article_id,
            # 'q_s': q_s,
            'quantity': quantity,
            'product': product,
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
