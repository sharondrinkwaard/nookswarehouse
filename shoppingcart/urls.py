from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('overview_orders/', views.overview_orders, name='overview_orders'),
    path('add_to_cart/<article_id>', views.add_to_cart, name='add_to_cart'),
    path('edit_cart/<article_id>', views.edit_cart, name='edit_cart'),
    path('delete_from_cart/<article_id>', views.delete_from_cart, name='delete_from_cart'),
]
