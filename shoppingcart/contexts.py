
def shopping_content(request):

    shopping_items = []
    total = 0
    product_count = 0
    delivery = 0

    grand_total = total + delivery

    context = {
        'shopping_items': shopping_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
