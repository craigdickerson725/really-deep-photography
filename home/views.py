from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.urls import reverse_lazy
import json
import stripe
from .models import Photo, Cart, CartItem, Order, OrderItem
from .forms import CheckoutForm, PhotoForm

# Initialize Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

# Home view
def index(request):
    """Query for featured photos and render the home page."""
    featured_photos = Photo.objects.filter(is_featured=True)[:3]
    return render(request, 'home/index.html', {'featured_photos': featured_photos})

# Gallery view
class GalleryView(ListView):
    """Display all photos in the gallery."""
    model = Photo
    template_name = 'home/gallery.html'
    context_object_name = 'photos'
    paginate_by = 3  # Show 3 photos per page

# About view
class AboutView(TemplateView):
    """Render the about page."""
    template_name = 'home/about.html'

# Contact view
class ContactView(TemplateView):
    """Render the contact page."""
    template_name = 'home/contact.html'

# Search view
def search(request):
    """Handle search queries and render results."""
    query = request.GET.get('q')
    if query:
        photos = Photo.objects.filter(title__icontains=query) | Photo.objects.filter(description__icontains=query)
    else:
        photos = []
        messages.warning(request, "Please enter a search term.")
    return render(request, 'home/search_results.html', {
        'query': query,
        'photos': photos
    })

# Photo detail view
def photo_detail(request, photo_id):
    """Display the details of a single photo."""
    photo = get_object_or_404(Photo, id=photo_id)
    return render(request, 'home/photo_detail.html', {'photo': photo})

# Admin panel 
class AdminPanelView(UserPassesTestMixin, View):
    template_name = 'home/admin_panel.html'  # Update to the full path
    login_url = reverse_lazy('account_login')  # Redirect to the login page if not logged in

    def test_func(self):
        # Check if user is authenticated and either a superuser or belongs to the 'Site Admin' group
        return self.request.user.is_authenticated and (self.request.user.is_superuser or self.request.user.groups.filter(name='Site Admin').exists())

    def handle_no_permission(self):
        # Redirect unauthorized users to a 'no permission' page
        return redirect('no_permission')

    def get(self, request):
        photos = Photo.objects.all()
        form = PhotoForm()  # Display a blank form on the get request
        return render(request, self.template_name, {'photos': photos, 'form': form})

    def post(self, request):
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')  # Redirect back to the admin panel on successful save
        photos = Photo.objects.all()
        return render(request, self.template_name, {'photos': photos, 'form': form})

class NoPermissionView(TemplateView):
    template_name = "home/no_permission.html"  # Updated path to include 'home'

class EditPhotoView(View):
    template_name = 'edit_photo.html'  # Create this template

    def get(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)
        form = PhotoForm(instance=photo)
        return render(request, self.template_name, {'form': form, 'photo': photo})

    def post(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
        return render(request, self.template_name, {'form': form, 'photo': photo})

class DeletePhotoView(View):
    def post(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)
        photo.delete()
        return redirect('admin_panel')


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
    return redirect('view_cart')

# View cart
@login_required
def view_cart(request):
    """Display the current items in the cart and total price."""
    cart = get_object_or_404(Cart, user=request.user)
    items = cart.items.all()
    total_quantity = sum(item.quantity for item in items)
    total_price = sum(item.subtotal for item in items)
    return render(request, 'home/cart.html', {
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
    return redirect('view_cart')

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
    return redirect('view_cart')

# Checkout view
@login_required
def checkout_view(request):
    """Render the checkout page with the form and total amount."""
    cart = get_object_or_404(Cart, user=request.user)
    cart_items = cart.items.all()
    total_amount = sum(item.subtotal for item in cart_items)

    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Process payment intent creation here
            return redirect('create_payment_intent')  # Redirect to create payment intent
    else:
        form = CheckoutForm()

    context = {
        'form': form,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
        'cart_items': cart_items,
        'total_amount': total_amount,
    }
    return render(request, 'home/checkout.html', context)

# Cache Checkout Data view
@login_required
def cache_checkout_data(request):
    """Cache checkout data temporarily in the PaymentIntent's metadata."""
    if request.method == 'POST':
        try:
            pid = request.POST.get('client_secret').split('_secret')[0]
            stripe.PaymentIntent.modify(pid, metadata={
                'user_id': request.user.id,
                'cart_id': request.user.cart.id,
                'billing_name': request.POST.get('billing_name'),
            })
            return HttpResponse(status=200)
        except Exception as e:
            return HttpResponse(content=e, status=400)

# Create Payment Intent for Stripe
@login_required
def create_payment_intent(request):
    """Create a Stripe Payment Intent for the cart total."""
    if request.method == 'POST':
        try:
            cart = get_object_or_404(Cart, user=request.user)
            total_amount = sum(item.subtotal for item in cart.items.all()) * 100  # Stripe uses cents

            # Create the payment intent
            intent = stripe.PaymentIntent.create(
                amount=int(total_amount),
                currency="usd",
                payment_method_types=["card"],
                metadata={'user_id': request.user.id},
            )
            return JsonResponse({'clientSecret': intent['client_secret']})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)

# Checkout success view
@login_required
def checkout_success(request):
    """Save order details after payment is confirmed and redirect to order confirmation."""
    if request.method == 'POST':
        try:
            # Load the data from the request body
            data = json.loads(request.body)

            # Print data for debugging
            print(f"Checkout data received: {data}")

            # Get the user's cart
            cart = get_object_or_404(Cart, user=request.user)

            # Create the Order
            order = Order.objects.create(
                user=request.user,
                billing_name=data['billing_name'],
                billing_address_1=data['billing_address_1'],
                billing_city=data['billing_city'],
                billing_state=data['billing_state'],
                billing_zip_code=data['billing_zip_code'],
                billing_country=data['billing_country'],
                total_amount=sum(item.subtotal for item in cart.items.all()),
                shipping_address_1=data.get('shipping_address_1') if not data.get('shipping_address_same') else None,
                shipping_city=data.get('shipping_city') if not data.get('shipping_address_same') else None,
                shipping_state=data.get('shipping_state') if not data.get('shipping_address_same') else None,
                shipping_zip_code=data.get('shipping_zip_code') if not data.get('shipping_address_same') else None,
                shipping_country=data.get('shipping_country') if not data.get('shipping_address_same') else None,
                payment_intent_id=data['payment_intent_id'],
            )

            print(f"Order created: {order}")

            # Create OrderItems from cart items
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    photo=item.photo,
                    quantity=item.quantity,
                    subtotal=item.subtotal
                )

            # Clear the cart after creating the order
            cart.items.all().delete()

            # Redirect to order confirmation page
            return redirect('order_confirmation', payment_intent_id=order.payment_intent_id)

        except json.JSONDecodeError:
            return redirect('home')

        except Exception as e:
            print(f"Error processing checkout: {e}")
            return redirect('home')

    return redirect('home')

# Order confirmation view
@login_required
def order_confirmation(request, payment_intent_id):
    # Attempt to retrieve the order based on the payment_intent_id
    order = get_object_or_404(Order, payment_intent_id=payment_intent_id)
    context = {
        'order': order,
    }
    return render(request, 'home/order_confirmation.html', context)
