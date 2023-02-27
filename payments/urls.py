from django.urls import path
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.payments, name='payments'),
    path('payment_succes/<order_number>', views.payment_succes, name='payment_succes'),
    path('wh/', webhook, name='webhook')
]
