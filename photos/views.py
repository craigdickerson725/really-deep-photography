from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, TemplateView, View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import Photo
from .forms import PhotoForm
from faq.models import FAQ
from faq.forms import FAQForm


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


# Admin panel
class AdminPanelView(UserPassesTestMixin, View):
    template_name = 'photos/admin_panel.html'

    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_superuser or self.request.user.groups.filter(name='Site Admin').exists()
        )

    def handle_no_permission(self):
        return redirect('no_permission')

    def get(self, request):
        photos = Photo.objects.all()
        form = PhotoForm()
        faq_form = FAQForm()
        faqs = FAQ.objects.all()
        featured_photos_count = Photo.objects.filter(is_featured=True).count()

        return render(request, self.template_name, {
            'photos': photos,
            'form': form,
            'faq_form': faq_form,
            'faqs': faqs,
            'featured_photos_count': featured_photos_count,
        })

    def post(self, request):
        if 'faq_form' in request.POST:
            # Handle FAQ Form Submission
            faq_form = FAQForm(request.POST)
            if faq_form.is_valid():
                faq_form.save()
                messages.success(request, "FAQ successfully added.")
                return redirect('admin_panel')

        elif 'faq_update' in request.POST:
            # Handle FAQ Update
            faq_id = request.POST.get('faq_id')
            faq_instance = FAQ.objects.get(id=faq_id)
            faq_form = FAQForm(request.POST, instance=faq_instance)
            if faq_form.is_valid():
                faq_form.save()
                messages.success(request, "FAQ successfully updated.")
                return redirect('admin_panel')

        elif 'faq_delete' in request.POST:
            # Handle FAQ Deletion
            faq_id = request.POST.get('faq_id')
            FAQ.objects.filter(id=faq_id).delete()
            messages.success(request, "FAQ successfully deleted.")
            return redirect('admin_panel')

        photos = Photo.objects.all()
        faqs = FAQ.objects.all()
        return render(request, self.template_name, {
            'photos': photos,
            'form': PhotoForm(),
            'faq_form': FAQForm(),
            'faqs': faqs,
        })


# No Permission View
class NoPermissionView(TemplateView):
    template_name = "photos/no_permission.html"


# Edit Photo View
class EditPhotoView(View):
    template_name = 'photos/edit_photo.html'  # Correct template path

    def dispatch(self, request, *args, **kwargs):
        # Restrict to superusers or 'Site Admin' group members
        if not (request.user.is_authenticated and (
            request.user.is_superuser or request.user.groups.filter(name='Site Admin').exists()
        )):
            return redirect('no_permission')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)
        form = PhotoForm(instance=photo)

        # Count featured photos
        featured_photos_count = Photo.objects.filter(is_featured=True).count()

        return render(request, self.template_name, {
            'form': form,
            'photo': photo,
            # Pass count to template
            'featured_photos_count': featured_photos_count,
        })

    def post(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            messages.info(self.request, 'Photo successfully edited')
            return redirect('admin_panel')
        return render(request, self.template_name, {'form': form, 'photo': photo})  # noqa


# Delete Photo View
class DeletePhotoView(View):

    def post(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)
        photo.delete()
        messages.info(self.request, 'Photo successfully deleted')
        return redirect('admin_panel')
