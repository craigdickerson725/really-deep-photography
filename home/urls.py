from django.urls import path
from . import webhooks
from cart.views import create_payment_intent
from .views import (
    index, AboutView, ContactView,
    checkout_view, checkout_success, cache_checkout_data,
)

urlpatterns = [
    # Home page
    path('', index, name='home'),

    # Static pages
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),

    # Checkout and payment
    path('checkout/', checkout_view, name='checkout'),
    path('cache-checkout-data/', cache_checkout_data, name='cache_checkout_data'),
    path('checkout-success/', checkout_success, name='checkout_success'),

    # Webhook for Stripe
    path('webhook/', webhooks.stripe_webhook, name='stripe_webhook'),
]
