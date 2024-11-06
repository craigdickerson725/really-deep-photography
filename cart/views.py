from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from photos.models import Photo

# View cart
def view_cart(request):
    """ Renders the cart contents page """
    cart = request.session.get('cart', {})
    cart_items = []

    # Populate cart items with photos and quantities
    for photo_id, quantity in cart.items():
        photo = get_object_or_404(Photo, pk=photo_id)
        cart_items.append({
            'photo': photo,
            'quantity': quantity,
            'photo_id': photo_id  # Ensure this key name is consistent with naming conventions
        })

    # Pass cart_items to the template
    return render(request, 'cart/cart.html', {'cart_items': cart_items})

# Add to cart
def add_to_cart(request, photo_id):
    """ Add a specified quantity of the selected photo to the cart """
    photo = get_object_or_404(Photo, id=photo_id)
    quantity = int(request.POST.get('quantity', 1))  # Default to 1 if quantity is not provided
    redirect_url = request.POST.get('redirect_url', reverse('view_cart'))  # Default to cart view if not provided
    cart = request.session.get('cart', {})

    if photo_id in cart:
        cart[photo_id] += quantity
        messages.success(request, f'Updated {photo.title} quantity to {cart[photo_id]}')
    else:
        cart[photo_id] = quantity
        messages.success(request, f'Added {photo.title} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)

# Adjust cart
def adjust_cart(request, photo_id):
    """Adjust the quantity of the specified photo to the specified amount"""
    photo = get_object_or_404(Photo, pk=photo_id)
    quantity = int(request.POST.get('quantity', 1))  # Default to 1 if no quantity is provided
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[photo_id] = quantity
        messages.success(request, f'Updated {photo.title} quantity to {cart[photo_id]}')
    else:
        cart.pop(photo_id, None)  # Remove item if quantity is 0 or invalid
        messages.success(request, f'Removed {photo.title} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

# Remove from cart
def remove_from_cart(request, photo_id):
    """Remove the specified photo from the cart"""
    try:
        photo = get_object_or_404(Photo, pk=photo_id)
        cart = request.session.get('cart', {})

        # Remove the item from the cart
        if str(photo_id) in cart:
            del cart[str(photo_id)]
        
        request.session['cart'] = cart  # Update the session with the new cart
        return JsonResponse({'status': 'success'})  # Return success response in JSON format

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
