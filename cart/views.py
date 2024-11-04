from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.http import JsonResponse
from .models import Cart, CartItem
from photos.models import Photo

# Add to cart
@login_required
def add_to_cart(request, photo_id):
    """Add a photo to the shopping cart."""
    photo = get_object_or_404(Photo, id=photo_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, photo=photo)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart:view_cart')  # Updated redirect

# View cart
@login_required
def view_cart(request):
    """Display the current items in the cart and total price."""
    cart, created = Cart.objects.get_or_create(user=request.user)  # Create cart if it doesn't exist
    items = cart.items.all()
    total_quantity = sum(item.quantity for item in items)
    total_price = sum(item.subtotal for item in items)
    
    if not items:
        # Optionally handle the case where the cart is empty
        return render(request, 'cart/cart.html', {
            'cart': cart,
            'items': items,
            'total_quantity': total_quantity,
            'total_price': total_price,
            'empty_cart': True,  # Flag to indicate cart is empty
        })

    return render(request, 'cart/cart.html', {
        'cart': cart,
        'items': items,
        'total_quantity': total_quantity,
        'total_price': total_price,
    })

# Remove from cart
@login_required
def remove_from_cart(request, cart_item_id):
    """Remove a specific item from the cart."""
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('cart:view_cart')  # Updated redirect

# Update cart
@login_required
def update_cart(request, cart_item_id):
    """Update the quantity of an item in the cart."""
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        if quantity.isdigit() and int(quantity) > 0:
            cart_item.quantity = int(quantity)
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart:view_cart')  # Updated redirect
