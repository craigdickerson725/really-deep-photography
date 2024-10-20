from django.shortcuts import render

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
