from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('overview_orders/', views.overview_orders, name='overview_orders'),
]


