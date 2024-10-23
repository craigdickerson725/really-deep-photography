from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.contrib.auth.decorators import login_required
from .models import Photo, Cart, CartItem

# Home view
def index(request):
    return render(request, 'home/index.html')

# Gallery view
class GalleryView(ListView):
    model = Photo
    template_name = 'home/gallery.html'
    context_object_name = 'photos'

# About view
class AboutView(TemplateView):
    template_name = 'home/about.html'

# Contact view
class ContactView(TemplateView):
    template_name = 'home/contact.html'

# Search view
def search(request):
    query = request.GET.get('q')
    # Search logic
    return render(request, 'home/search_results.html', {'query': query})

# Photo details view
def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    return render(request, 'home/photo_detail.html', {'photo': photo})

@login_required
# Add to cart
def add_to_cart(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, photo=photo)
    if not created:  # If the item already exists, increase the quantity
        cart_item.quantity += 1
        cart_item.save()

    return redirect('view_cart')  # Redirect to the cart view

# Cart view
@login_required
def view_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    items = cart.items.all()  # Get all CartItems related to the user's cart
    total = sum(item.photo.price * item.quantity for item in items)

    return render(request, 'home/cart.html', {'cart': cart, 'items': items, 'total': total})

# Remove from cart
@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')  # Redirect to the cart view

# Update cart
@login_required
def update_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        if quantity.isdigit() and int(quantity) > 0:
            cart_item.quantity = int(quantity)
            cart_item.save()
        else:
            cart_item.delete()  # Remove item if quantity is invalid or 0
    return redirect('view_cart')  # Redirect to the cart view
    