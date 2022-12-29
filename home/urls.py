from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('home/', views.index, name='index'),
    path('overview_orders/', views.overview_orders, name='overview_orders'),

]
