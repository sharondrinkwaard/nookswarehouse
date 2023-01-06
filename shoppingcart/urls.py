from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('overview_orders/', views.overview_orders, name='overview_orders'),
    path('add/<article_id>', views.add_to_cart, name='add_to_cart'),
]
