from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from photos.models import Photo


# View cart
@login_required
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
            'photo_id': photo_id
        })

    # Pass cart_items to the template
    return render(request, 'cart/cart.html', {'cart_items': cart_items})


# Add to cart
@login_required
def add_to_cart(request, photo_id):
    """ Add a specified quantity of the selected photo to the cart """
    photo = get_object_or_404(Photo, id=photo_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get(
        'redirect_url', reverse('photo_detail', args=[photo_id])
    )
    cart = request.session.get('cart', {})
    str_photo_id = str(photo_id)

    if str_photo_id in cart:
        cart[str_photo_id] += quantity
    else:
        cart[str_photo_id] = quantity

    request.session['cart'] = cart
    cart_item_count = sum(cart.values())
    messages.success(request, f'Added {photo.title} to your cart!')

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({'cart_item_count': cart_item_count})

    return redirect(redirect_url)


# Adjust cart
def adjust_cart(request, photo_id):
    """ Adjust the quantity of the specified photo to the specified amount """
    photo = get_object_or_404(Photo, pk=photo_id)
    quantity = int(request.POST.get('quantity', 1))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[photo_id] = quantity
        messages.success(
            request, f"Quantity of {photo.title} updated to {quantity}."
        )
    else:
        cart.pop(photo_id, None)
        messages.success(request, f"{photo.title} removed from your cart.")

    request.session['cart'] = cart
    return redirect('view_cart')


# Remove from cart
def remove_from_cart(request, photo_id):
    """ Remove the specified photo from the cart """
    try:
        photo = get_object_or_404(Photo, pk=photo_id)
        cart = request.session.get('cart', {})

        if str(photo_id) in cart:
            del cart[str(photo_id)]
            messages.success(request, f"{photo.title} removed from your cart.")

        request.session['cart'] = cart
        request.session.modified = True
        return redirect('view_cart')

    except Exception as e:
        messages.error(request, f"Error removing item: {str(e)}")
        return redirect('view_cart')
