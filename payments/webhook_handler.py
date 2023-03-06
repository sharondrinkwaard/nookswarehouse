from django.http import HttpResponse
from .models import Order, OrderLineItem
from django.conf import settings
from products.models import Product
from django.template.loader import render_to_string

import json
import time


class StripeWH_Handler:
    ''' Handle Stripe Webhooks '''

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        ''' Handle a webhook event '''
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        ''' Handle succeeded webhook from Stripe '''
        intent = event.data.object
        print(intent)
        pid = intent.id
        cart = intent.metadata.cart
        save_info = intent.metadata.save_info
        # stripe_charge = stripe.Charge.retrieve(
        #     intent.latest_charge
        # )
        # billing_details = stripe_charge.billing_details
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        # grand_total = round(stripe_charge.amount / 100, 2)
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Replace empty strings with None
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        # update profile information
        # profile = None
        # username = intent.metadata.username
        # if username != 'AnonymousUser':
        #     profile = UserProfile.objects.get(user__username=username)
        #     if save_info:
        #         profile.default_phone_number = shipping_details.phone
        #         profile.default_country = shipping_details.address.country
        #         profile.default_postcode = shipping_details.address.postal_code
        #         profile.default_town_or_city = shipping_details.address.city
        #         profile.default_street_address1 = shipping_details.address.line1
        #         profile.default_street_address2 = shipping_details.address.line2
        #         profile.default_county = shipping_details.address.state
        #         profile.save()

        order_existence = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    first_name__iexact=shipping_details.first_name,
                    last_name__iexact=shipping_details.last_name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=shipping_details.phone_number,
                    postcode__iexact=shipping_details.address.postcode,
                    city__iexact=shipping_details.address.city,
                    street_address__iexact=shipping_details.address.street_address,
                    house_number__iexact=shipping_details.address.house_number,
                    county__iexact=shipping_details.address.county,
                    country__iexact=shipping_details.address.country,
                    grand_total=grand_total,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                order_existence = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_existence:
            # self._send_confirmation_email(order)
            return HttpResponse(
                content=f'Webhook received: {event["type"]} SUCCES! Order in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    first_name=shipping_details.first_name,
                    last_name=shipping_details.last_name,
                    email=billing_details.email,
                    phone_number=shipping_details.phone_number,
                    postcode=shipping_details.address.postcode,
                    city=shipping_details.address.city,
                    street_address=shipping_details.address.street_address,
                    house_number=shipping_details.address.house_number,
                    county=shipping_details.address.county,
                    country=shipping_details.address.country,
                    original_cart=cart,
                    stripe_pid=pid,
                )
                for article_id, item_data in json.loads(cart).items():
                    product = Product.objects.get(id=article_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                product_size=size,
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                    return HttpResponse(
                        content=f'Webhook received: {event["type"]} ERROR {e}',
                        status=500)
        # self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_failed(self, event):
        ''' Handle failed webhook '''
        return HttpResponse(
                content=f'Webhook received: {event["type"]}',
                status=200)
