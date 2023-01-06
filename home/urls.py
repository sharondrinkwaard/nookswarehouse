from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='index'),
    path('service/', views.customer_service, name='customer_service'),
]
