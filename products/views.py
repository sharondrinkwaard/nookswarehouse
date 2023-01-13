from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
# Q handles queries
from django.db.models import Q
from .models import Product, Category, QuantitySize
from .forms import ProductSize, ProductQuantity, ProductColor
from django.views import View


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    categories = None
    query = None

    # Gets the category/search request and displays the correct products
    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'request' in request.GET:
            query = request.GET['request']
            if not query:
                message.error(request, 'Enter search criteria')
                return redirect(reverse('products'))

            # Queries in name OR description instead of both
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            # Filters out the queries so only queries are displayed
            products = products.filter(queries)

    context = {
        'products': products,
        'search_request': query,
        'current_cat': categories,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """

    product = get_object_or_404(Product, pk=product_id)
    form_size = ProductSize()
    form_quanity = ProductQuantity()
    form_color = ProductColor()

    context = {
        'product': product,
        'form_size': form_size,
        'form_quantity': form_quanity,
        'form_color': form_color,
        }

    return render(request, 'products/product_detail.html', context)


class QuantitySizeColor(View):

    # def post(self, request):
    #     q = ProductQuantity(request.POST)
        
    #     if q.is_valid():
    #         add_q = q.save(commit=False)
    #         add_q.save()
    #         return redirect('redirect_url')
    #     else:
    #         render(request, 'products.html', {'q': q})

    def post_size(self, request):
        s = ProductSize(request.POST)
        if s.is_valid():
            add_s = s.save(commit=False)
            add_s.save()
            return redirect('redirect_url')
        else:
            render(request, 'products.html', {'s': s})
