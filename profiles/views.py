from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from django.contrib import messages
from payments.models import Order
from .forms import ProfileForm


def profiles(request):
    ''' View the users profile '''
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Profile updated')
        else:
            # messages.error(request, 'Update failed. Try again')
            print('Update failed, try again')
    else:
        form = ProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profiles.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)
