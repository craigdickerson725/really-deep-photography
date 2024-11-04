from django.shortcuts import render
from django.views.generic import TemplateView
from photos.models import Photo

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
    