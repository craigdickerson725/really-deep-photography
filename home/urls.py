from django.urls import path
from .views import (
    index, GalleryView, AboutView, ContactView, search, photo_detail, 
    add_to_cart, view_cart, remove_from_cart, update_cart, checkout_view,
    create_payment_intent, confirm_order, order_confirmation  # Import the confirm_order and order_confirmation views
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

    # Cart operations
    path('add-to-cart/<int:photo_id>/', add_to_cart, name='add_to_cart'),
    path('view-cart/', view_cart, name='view_cart'),
    path('remove-from-cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('update-cart/<int:cart_item_id>/', update_cart, name='update_cart'),

    # Checkout and payment
    path('checkout/', checkout_view, name='checkout'),
    path('create-payment-intent/', create_payment_intent, name='create_payment_intent'),
    path('confirm-order/', confirm_order, name='confirm_order'),

    # Order confirmation
    path('confirmation/<int:order_id>/', order_confirmation, name='order_confirmation'),
]
