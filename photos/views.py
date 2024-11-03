from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView, View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Photo
from .forms import PhotoForm

# Gallery view
class GalleryView(ListView):
    """Display all photos in the gallery."""
    model = Photo
    template_name = 'photos/gallery.html'  # Correct template path
    context_object_name = 'photos'
    paginate_by = 3  # Show 3 photos per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_obj'] = context['paginator'].get_page(context['page_obj'].number)
        return context

    def get_queryset(self):
        return Photo.objects.all().order_by("id")

# Search view
def search(request):
    """Handle search queries and render results."""
    query = request.GET.get('q')
    if query:
        photos = Photo.objects.filter(title__icontains=query) | Photo.objects.filter(description__icontains=query)
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

# Admin panel 
class AdminPanelView(UserPassesTestMixin, View):
    template_name = 'photos/admin_panel.html'  # Correct template path

    def test_func(self):
        # Check if user is authenticated and either a superuser or belongs to the 'Site Admin' group
        return self.request.user.is_authenticated and (self.request.user.is_superuser or self.request.user.groups.filter(name='Site Admin').exists())

    def handle_no_permission(self):
        # Redirect unauthorized users to a 'no permission' page
        return redirect('no_permission')

    def get(self, request):
        photos = Photo.objects.all()
        form = PhotoForm()  # Display a blank form on the get request
        return render(request, self.template_name, {'photos': photos, 'form': form})

    def post(self, request):
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')  # Redirect back to the admin panel on successful save
        photos = Photo.objects.all()
        return render(request, self.template_name, {'photos': photos, 'form': form})

# No Permission View
class NoPermissionView(TemplateView):
    template_name = "photos/no_permission.html"

# Edit Photo View
class EditPhotoView(View):
    template_name = 'photos/edit_photo.html'  # Correct template path

    def get(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)
        form = PhotoForm(instance=photo)
        return render(request, self.template_name, {'form': form, 'photo': photo})

    def post(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            return redirect('admin_panel')
        return render(request, self.template_name, {'form': form, 'photo': photo})

# Delete Photo View
class DeletePhotoView(View):
    def post(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)
        photo.delete()
        return redirect('admin_panel')
