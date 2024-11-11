from django.contrib import messages
from django.shortcuts import render
from photos.models import Photo

# Home view
def index(request):
    """Query for featured photos and render the home page."""
    # Get featured photos
    featured_photos = Photo.objects.filter(is_featured=True)[:3]
    # Filter out cart-related messages (those containing 'Added' or 'Updated')
    filtered_messages = [msg for msg in messages.get_messages(request) if 'Added' not in msg.message and 'Updated' not in msg.message]

    return render(request, 'home/index.html', {'featured_photos': featured_photos, 'messages': filtered_messages})
