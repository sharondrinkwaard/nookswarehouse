from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')
