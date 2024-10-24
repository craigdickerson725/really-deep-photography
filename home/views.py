from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from .models import Photo, Cart, CartItem

# Home view
def index(request):
    # Query for featured photos
    featured_photos = Photo.objects.filter(is_featured=True)[:3]
    return render(request, 'home/index.html', {'featured_photos': featured_photos})

# Gallery view
class GalleryView(ListView):
    """ Display all photos in the gallery. """
    model = Photo
    template_name = 'home/gallery.html'
    context_object_name = 'photos'

# About view
class AboutView(TemplateView):
    """ Render the about page. """
    template_name = 'home/about.html'

# Contact view
class ContactView(TemplateView):
    """ Render the contact page. """
    template_name = 'home/contact.html'

# Search view
def search(request):
    """ Handle search queries and render results. """
    query = request.GET.get('q')
    photos = Photo.objects.filter(title__icontains=query) if query else []
    return render(request, 'home/search_results.html', {
        'query': query,
        'photos': photos
    })

# Photo details view
def photo_detail(request, photo_id):
    """ Display detailed view of a specific photo. """
    photo = get_object_or_404(Photo, id=photo_id)
    return render(request, 'home/photo_detail.html', {'photo': photo})

# Add to cart
@login_required
def add_to_cart(request, photo_id):
    """ Add a photo to the shopping cart. """
    photo = get_object_or_404(Photo, id=photo_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if the photo is already in the cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, photo=photo)
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    return redirect('view_cart')

# View cart
@login_required
def view_cart(request):
    """ Display the current items in the cart and total price. """
    cart = get_object_or_404(Cart, user=request.user)
    items = cart.items.all()

    # Calculate total by summing the subtotals of all items
    total = sum(item.get_total_price() for item in items)

    return render(request, 'home/cart.html', {
        'cart': cart,
        'items': items,
        'total': total,
    })

# Remove from cart
@login_required
def remove_from_cart(request, cart_item_id):
    """ Remove a specific item from the cart. """
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')

# Update cart
@login_required
def update_cart(request, cart_item_id):
    """ Update the quantity of an item in the cart. """
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        if quantity.isdigit() and int(quantity) > 0:
            cart_item.quantity = int(quantity)
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('view_cart')

# Checkout view
def checkout(request):
    """ Render the checkout page. """
    return render(request, 'home/checkout.html')
