from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.contrib import messages
from .models import Photo


# Gallery view
class GalleryView(ListView):
    """Display all photos in the gallery."""
    model = Photo
    template_name = 'photos/gallery.html'  # Correct template path
    context_object_name = 'photos'
    paginate_by = 3  # Show 3 photos per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_obj'] = context['paginator'].get_page(context['page_obj'].number)  # noqa
        return context

    def get_queryset(self):
        return Photo.objects.all().order_by("id")


# Search view
def search(request):
    """Handle search queries and render results."""
    query = request.GET.get('q')
    if query:
        photos = Photo.objects.filter(title__icontains=query) | Photo.objects.filter(description__icontains=query)  # noqa
    else:
        photos = []
        messages.warning(request, "Please enter a search term.")
    return render(request, 'photos/search_results.html', {
        'query': query,
        'photos': photos
    })


# Photo detail view
def photo_detail(request, photo_id):
    """Display the details of a single photo."""
    photo = get_object_or_404(Photo, id=photo_id)
    return render(request, 'photos/photo_detail.html', {'photo': photo})
