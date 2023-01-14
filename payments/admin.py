from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number', 'date',
                       'delivery_costs', 'order_total',
                       'grand_total',)

    fields = ('order_number', 'date', 'first_name', 'last_name',
              'email', 'phone_number', 'country',
              'street_address', 'house_number', 'postcode', 'city',
              'county', 'delivery_costs',
              'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'last_name',
                    'order_total', 'delivery_costs',
                    'grand_total',)

    sorting = ('-date',)


admin.site.register(Order, OrderAdmin)
