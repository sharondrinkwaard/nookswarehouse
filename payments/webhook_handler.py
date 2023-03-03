from django.http import HttpResponse


class StripeWH_Handler:
    '''' Handle Stripe Webhooks '''

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        ''' Handle a webhook event '''
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_succeeded(self, event):
        '''' Handle succeeded webhook from Stripe '''
        intent = event.data.object
        print(intent)
        return HttpResponse(
                content=f'Webhook received: {event["type"]}',
                status=200)

    def handle_payment_intent_failed(self, event):
        ''' Handle failed webhook '''
        return HttpResponse(
                content=f'Webhook received: {event["type"]}',
                status=200)
