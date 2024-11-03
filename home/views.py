from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse, HttpResponse
import stripe
from .models import Order, OrderItem
from .forms import CheckoutForm
from photos.models import Photo

# Initialize Stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

# Home view
def index(request):
    """Query for featured photos and render the home page."""
    featured_photos = Photo.objects.filter(is_featured=True)[:3]
    return render(request, 'home/index.html', {'featured_photos': featured_photos})

# About view
class AboutView(TemplateView):
    """Render the about page."""
    template_name = 'home/about.html'

# Contact view
class ContactView(TemplateView):
    """Render the contact page."""
    template_name = 'home/contact.html'
    
# Cache Checkout Data view
@login_required
def cache_checkout_data(request):
    """Cache checkout data temporarily in the PaymentIntent's metadata."""
    if request.method == 'POST':
        try:
            pid = request.POST.get('client_secret').split('_secret')[0]
            stripe.api_key = settings.STRIPE_SECRET_KEY
            stripe.PaymentIntent.modify(pid, metadata={
                'user_id': request.user.id,
                'cart_id': request.user.cart.id,
                'billing_name': request.POST.get('billing_name'),
            })
            return HttpResponse(status=200)
        except Exception as e:
            return HttpResponse(content=e, status=400)

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
            order = Order(
                user=request.user,
                billing_name=form.cleaned_data['billing_name'],
                billing_address_1=form.cleaned_data['billing_address_1'],
                billing_city=form.cleaned_data['billing_city'],
                billing_state=form.cleaned_data['billing_state'],
                billing_zip_code=form.cleaned_data['billing_zip_code'],
                billing_country=form.cleaned_data['billing_country'],
                total_amount=total_amount,  # Use calculated total amount
                payment_intent_id='pending'  # Placeholder until payment is processed
            )
            order.save()

            # Create OrderItems based on the cart items
            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    photo=item.photo,
                    quantity=item.quantity,
                )

            # Save the order ID in the session for later use
            request.session['order_id'] = order.id

            # Process payment intent creation here
            return redirect('create_payment_intent')  # Redirect to create payment intent
        else:
            messages.error(request, 'There was an error with your form. Please double check your information.')
    else:
        form = CheckoutForm()

    context = {
        'form': form,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
        'cart_items': cart_items,
        'total_amount': total_amount,
    }
    return render(request, 'home/checkout.html', context)

# Checkout success view
@login_required
def checkout_success(request):
    """Render the success page after payment is confirmed, save the order, and clear the cart."""
    # Retrieve the order ID from the session
    order_id = request.session.get('order_id')

    if order_id:
        # Retrieve the order
        order = get_object_or_404(Order, id=order_id)

        # Confirm payment status
        payment_intent_id = request.POST.get('payment_intent_id')  # Get from the POST request
        if payment_intent_id:
            # Update order with payment intent ID and status
            order.payment_intent_id = payment_intent_id
            order.save()

            # Clear the cart items after saving the order
            CartItem.objects.filter(cart=order.user.cart).delete()

            # Clear the order_id from the session to avoid reuse
            del request.session['order_id']

            # Send a confirmation email
            try:
                send_mail(
                    subject=f'Order Confirmation - Order #{order.id}',
                    message=f'Thank you for your order, {order.billing_name}! Your order number is {order.id}.',
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[request.user.email],
                    fail_silently=False,
                )
                print(f"Confirmation email sent to {request.user.email}.")
            except Exception as e:
                print(f"Failed to send email: {e}")

            messages.success(request, f'Order successfully processed! Your order number is {order.id}. A confirmation email has been sent to {request.user.email}.')
            
            # Render the success page
            context = {'order': order}
            return render(request, 'home/checkout_success.html', context)

    messages.error(request, "There was an issue with your order.")
    return redirect('home')  # Redirect to home if no order ID found
