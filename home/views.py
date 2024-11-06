from django.contrib import messages
from django.shortcuts import render
from django.views.generic import TemplateView
from photos.models import Photo

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
    """Render the contact page."""
    template_name = 'home/contact.html'
    