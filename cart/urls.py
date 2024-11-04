from django.urls import path
from .views import add_to_cart, view_cart, remove_from_cart, update_cart

app_name = 'cart'

urlpatterns = [
    path('add-to-cart/<int:photo_id>/', add_to_cart, name='add_to_cart'),
    path('view-cart/', view_cart, name='view_cart'),
    path('remove-from-cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('update-cart/<int:cart_item_id>/', update_cart, name='update_cart'),
]
