from django.shortcuts import render


def overview_orders(request):
    """ A view to display the orders made by the authenticated customer """
    return render(request, 'shoppingcart/overview_orders.html')
    