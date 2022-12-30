from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def overview_orders(request):
    """ A view to display the orders made by the authenticated customer """
    return render(request, 'overview_orders.html')


def customer_service(request):
    """ A view to direct to the customer service page """
    return render(request, 'service.html')
    