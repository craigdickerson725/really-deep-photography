from django.urls import path
from . import webhooks
from .views import (
    index, GalleryView, AboutView, ContactView, search, photo_detail, 
    add_to_cart, view_cart, remove_from_cart, update_cart, checkout_view,
    create_payment_intent, checkout_success, order_confirmation,
    cache_checkout_data, AdminPanelView, NoPermissionView,
    EditPhotoView, DeletePhotoView,
)

urlpatterns = [
    # Home page
    path('', index, name='home'),
    
    # Static pages
    path('gallery/', GalleryView.as_view(), name='gallery'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),

    # Search functionality
    path('search/', search, name='search'),
    
    # Photo details
    path('photo/<int:photo_id>/', photo_detail, name='photo_detail'),

    # Admin panel for site owner
    path('admin_panel/', AdminPanelView.as_view(), name='admin_panel'),
    path('admin_panel/edit/<int:photo_id>/', EditPhotoView.as_view(), name='edit_photo'),
    path('admin_panel/delete/<int:photo_id>/', DeletePhotoView.as_view(), name='delete_photo'),
    path('no_permission/', NoPermissionView.as_view(), name='no_permission'),

    # Cart operations
    path('add-to-cart/<int:photo_id>/', add_to_cart, name='add_to_cart'),
    path('view-cart/', view_cart, name='view_cart'),
    path('remove-from-cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('update-cart/<int:cart_item_id>/', update_cart, name='update_cart'),

    # Checkout and payment
    path('checkout/', checkout_view, name='checkout'),
    path('create-payment-intent/', create_payment_intent, name='create_payment_intent'),
    path('cache-checkout-data/', cache_checkout_data, name='cache_checkout_data'),
    path('checkout-success/', checkout_success, name='checkout_success'),

    # Order confirmation
    path('order-confirmation/<str:payment_intent_id>/', order_confirmation, name='order_confirmation'),

    # Webhook for Stripe
    path('webhook/', webhooks.stripe_webhook, name='stripe_webhook'),
]
