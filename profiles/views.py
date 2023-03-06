from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from django.contrib import messages
from payments.models import Order


def profiles(request):
    ''' View the users profile '''
    template = 'profiles/profiles.html'
    context = {}

    return render(request, template, context)