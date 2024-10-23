from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from .models import Photo

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
