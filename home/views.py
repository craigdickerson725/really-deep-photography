from django.contrib import messages
from django.shortcuts import render
from photos.models import Photo


# Home view
def index(request):
    """Query for featured photos and render the home page."""
    # Get featured photos
    featured_photos = Photo.objects.filter(is_featured=True)[:3]

    # Determine if the user is part of the "Site Admin" group
    is_site_admin = (
        request.user.is_authenticated
        and (request.user.is_superuser or request.user.groups.filter(name="Site Admin").exists())
    )

    # Render the template with the required context
    return render(
        request,
        'home/index.html',
        {
            'featured_photos': featured_photos,
            'is_site_admin': is_site_admin,
        }
    )

    # Filter out cart-related messages
    filtered_messages = []
    for msg in messages.get_messages(request):
        # Handle both standard and dictionary-based messages
        if hasattr(msg, 'message'):
            if 'Added' not in msg.message and 'Updated' not in msg.message:
                filtered_messages.append(msg)
        else:
            # If msg is a dictionary (e.g., in tests), just append it
            filtered_messages.append(msg)

    return render(request, 'home/index.html', {'featured_photos': featured_photos, 'messages': filtered_messages})  # noqa
