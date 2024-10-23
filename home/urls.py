from django.urls import path
from .views import (
    index, GalleryView, AboutView, ContactView, search, photo_detail, 
    add_to_cart, view_cart, remove_from_cart, update_cart, checkout
)

urlpatterns = [
    # Home page
    path('', index, name='home'),
    # Gallery page
    path('gallery/', GalleryView.as_view(), name='gallery'),
    # About page
    path('about/', AboutView.as_view(), name='about'),
    # Contact page
    path('contact/', ContactView.as_view(), name='contact'),
    # Search functionality
    path('search/', search, name='search'),
    # Photo details page
    path('photo/<int:photo_id>/', photo_detail, name='photo_detail'),
    # Add to cart
    path('add-to-cart/<int:photo_id>/', add_to_cart, name='add_to_cart'),
    # View cart
    path('view-cart/', view_cart, name='view_cart'),
    # Remove from cart
    path('remove-from-cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    # Update cart
    path('update-cart/<int:cart_item_id>/', update_cart, name='update_cart'),
    # Checkout page
    path('checkout/', checkout, name='checkout'),
]
