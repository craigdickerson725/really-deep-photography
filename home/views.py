from django.shortcuts import render
from django.views.generic import TemplateView

# Home view
def index(request):
    return render(request, 'home/index.html')

# Gallery view
class GalleryView(TemplateView):
    template_name = 'home/gallery.html'

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
