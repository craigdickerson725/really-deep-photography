from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from photos.models import Photo
from faq.models import FAQ
from photos.forms import PhotoForm
from faq.forms import FAQForm


class AdminPanelView(UserPassesTestMixin, View):
    """Admin panel main page"""
    template_name = 'admin_panel/admin_panel.html'

    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_superuser or self.request.user.groups.filter(name='Site Admin').exists()  # noqa
        )

    def handle_no_permission(self):
        return redirect('no_permission')

    def get(self, request):
        photos = Photo.objects.all()
        faqs = FAQ.objects.all()
        featured_photos_count = Photo.objects.filter(is_featured=True).count()
        return render(request, self.template_name, {
            'photos': photos,
            'faqs': faqs,
            'photo_form': PhotoForm(),  # Blank form for adding photos
            'faq_form': FAQForm(),      # Blank form for adding FAQs
            'featured_photos_count': featured_photos_count,
        })


class PhotoCRUDView(UserPassesTestMixin, View):
    """Add or manage photos"""

    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_superuser or self.request.user.groups.filter(name='Site Admin').exists()  # noqa
        )

    def handle_no_permission(self):
        return redirect('no_permission')

    def post(self, request):
        if 'add_photo' in request.POST:
            photo_form = PhotoForm(request.POST, request.FILES)
            if photo_form.is_valid():
                photo_form.save()
                messages.success(request, "Photo successfully added.")
            else:
                messages.error(request, "Failed to add photo. Check the form.")
        return redirect('admin_panel')


class EditPhotoView(UserPassesTestMixin, View):
    """Edit a photo"""
    template_name = 'admin_panel/edit_photo.html'

    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_superuser or self.request.user.groups.filter(name='Site Admin').exists()  # noqa
        )

    def handle_no_permission(self):
        return redirect('no_permission')

    def get(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)
        form = PhotoForm(instance=photo)
        return render(request, self.template_name, {'form': form, 'photo': photo})  # noqa

    def post(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)
        form = PhotoForm(request.POST, request.FILES, instance=photo)
        if form.is_valid():
            form.save()
            messages.success(request, "Photo successfully updated.")
            return redirect('admin_panel')
        messages.error(request, "Failed to update photo. Check the form.")
        return render(request, self.template_name, {'form': form, 'photo': photo})  # noqa


class DeletePhotoView(UserPassesTestMixin, View):
    """Delete a photo"""

    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_superuser or self.request.user.groups.filter(name='Site Admin').exists()  # noqa
        )

    def handle_no_permission(self):
        return redirect('no_permission')

    def post(self, request, photo_id):
        photo = get_object_or_404(Photo, id=photo_id)
        photo.delete()
        messages.success(request, "Photo successfully deleted.")
        return redirect('admin_panel')


class FAQCRUDView(UserPassesTestMixin, View):
    """Add or update an FAQ"""

    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_superuser or self.request.user.groups.filter(name='Site Admin').exists()  # noqa
        )

    def handle_no_permission(self):
        return redirect('no_permission')

    def post(self, request):
        if 'add_faq' in request.POST:
            faq_form = FAQForm(request.POST)
            if faq_form.is_valid():
                faq_form.save()
                messages.success(request, "FAQ successfully added.")
            else:
                messages.error(request, "Failed to add FAQ. Check the form.")
        elif 'update_faq' in request.POST:
            faq_id = request.POST.get('faq_id')
            faq_instance = get_object_or_404(FAQ, id=faq_id)
            faq_form = FAQForm(request.POST, instance=faq_instance)
            if faq_form.is_valid():
                faq_form.save()
                messages.success(request, "FAQ successfully updated.")
            else:
                messages.error(request, "Failed to update FAQ. Check the form.")  # noqa
        return redirect('admin_panel')


class FAQDeleteView(UserPassesTestMixin, View):
    """Delete an FAQ"""

    def test_func(self):
        return self.request.user.is_authenticated and (
            self.request.user.is_superuser or self.request.user.groups.filter(name='Site Admin').exists()  # noqa
        )

    def handle_no_permission(self):
        return redirect('no_permission')

    def post(self, request):
        faq_id = request.POST.get('faq_id')
        faq = get_object_or_404(FAQ, id=faq_id)
        faq.delete()
        messages.success(request, "FAQ successfully deleted.")
        return redirect('admin_panel')


class NoPermissionView(TemplateView):
    """Redirect unauthorized users"""
    template_name = "admin_panel/no_permission.html"
