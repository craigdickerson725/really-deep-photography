from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from photos.models import Photo
from .models import ContactMessage

# Home view
def index(request):
    """Query for featured photos and render the home page."""
    # Get featured photos
    featured_photos = Photo.objects.filter(is_featured=True)[:3]
    # Filter out cart-related messages (those containing 'Added' or 'Updated')
    filtered_messages = [msg for msg in messages.get_messages(request) if 'Added' not in msg.message and 'Updated' not in msg.message]

    return render(request, 'home/index.html', {'featured_photos': featured_photos, 'messages': filtered_messages})

# About view
class AboutView(TemplateView):
    """Render the about page."""
    template_name = 'home/about.html'

# Contact view
class ContactView(TemplateView):
    """Handle the contact form submission."""
    template_name = 'home/contact.html'

    def post(self, request, *args, **kwargs):
        # Save the message to the database
        ContactMessage.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message'],
        )
        # Display a success message
        messages.success(request, 'Thank you for reaching out! Your message has been sent.')
        return redirect('contact')

