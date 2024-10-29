# webhook_handler.py

import json
import stripe
from django.conf import settings
from django.http import HttpResponse
from .models import Order, User

class WebhookHandler:
    """Class to handle Stripe webhooks."""

    def __init__(self, request):
        self.request = request

    def handle_payment_intent_succeeded(self, event):
        """Handle successful payment intent events."""
        payment_intent = event['data']['object']
        payment_intent_id = payment_intent['id']
        metadata = payment_intent.get('metadata', {})
        
        # Log the payment intent ID
        print(f"Payment succeeded for intent: {payment_intent_id}")

        user_id = metadata.get('user_id')

        try:
            # Retrieve user
            user = User.objects.get(id=user_id)

            # Create an order
            order = Order.objects.create(
                user=user,
                total_amount=payment_intent['amount_received'] / 100,  # Amount in dollars
                payment_intent_id=payment_intent_id,
                billing_name=metadata.get('billing_name', ''),
                billing_address_1=metadata.get('billing_address_1', ''),
                billing_city=metadata.get('billing_city', ''),
                billing_state=metadata.get('billing_state', ''),
                billing_zip_code=metadata.get('billing_zip_code', ''),
                billing_country=metadata.get('billing_country', ''),
            )

            print(f"Order {order.id} created successfully.")
            return HttpResponse(status=200)

        except User.DoesNotExist:
            print(f"No user found with id {user_id}")
            return HttpResponse(status=404)
        except Exception as e:
            print(f"Error creating order: {str(e)}")
            return HttpResponse(status=500)

    def handle_payment_intent_failed(self, event):
        """Handle failed payment intent events."""
        payment_intent = event['data']['object']
        payment_intent_id = payment_intent['id']
        print(f"Payment failed for intent: {payment_intent_id}")
        return HttpResponse(status=200)

    def process_event(self, event):
        """Process the event received from Stripe."""
        event_type = event['type']
        if event_type == 'payment_intent.succeeded':
            return self.handle_payment_intent_succeeded(event)
        elif event_type == 'payment_intent.payment_failed':
            return self.handle_payment_intent_failed(event)

        print(f"Unhandled event type: {event_type}")
        return HttpResponse(status=200)
