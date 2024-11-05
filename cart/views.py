from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from photos.models import Photo

# Create your views here.

def view_cart(request):
    """ Renders the cart contents page """
    return render(request, 'cart/cart.html')

def add_to_cart(request, photo_id):
    """ Add a specified quantity of the selected photo to the cart """
    
    photo = get_object_or_404(Photo, pk=photo_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if photo_id in cart:
        cart[photo_id] += quantity
        messages.success(request, f'Updated {photo.name} quantity to {cart[photo_id]}')
    else:
        cart[photo_id] = quantity
        messages.success(request, f'Added {photo.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)

def adjust_cart(request, photo_id):
    """Adjust the quantity of the specified photo to the specified amount"""

    photo = get_object_or_404(Photo, pk=photo_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[photo_id] = quantity
        messages.success(request, f'Updated {photo.name} quantity to {cart[photo_id]}')
    else:
        cart.pop(photo_id)
        messages.success(request, f'Removed {photo.name} from your cart')

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))

def remove_from_cart(request, photo_id):
    """Remove the specified photo from the cart"""

    try:
        photo = get_object_or_404(Photo, pk=photo_id)
        cart = request.session.get('cart', {})

        cart.pop(photo_id)
        messages.success(request, f'Removed {photo.name} from your cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
