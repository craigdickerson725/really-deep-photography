# webhooks.py

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.conf import settings
import stripe
import json
from .models import Order
from .webhook_handler import WebhookHandler

# Initialize Stripe with your secret key
stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def stripe_webhook(request):
    """Handle incoming Stripe webhook events."""
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')

    # Log the incoming payload for debugging
    print("Received webhook payload:", payload.decode('utf-8'))

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        print(f"Invalid payload: {str(e)}")
        return JsonResponse({'error': str(e)}, status=400)
    except stripe.error.SignatureVerificationError as e:
        print(f"Invalid signature: {str(e)}")
        return JsonResponse({'error': str(e)}, status=400)

    # Create an instance of the webhook handler
    handler = WebhookHandler(request)
    return handler.process_event(event)
