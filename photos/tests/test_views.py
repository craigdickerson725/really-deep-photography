from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from photos.models import Photo  # Corrected import
from django.contrib.messages import get_messages

class PhotoViewsTests(TestCase):

    def setUp(self):
        # Create test user and photo instance
        self.user = get_user_model().objects.create_user(
            username='testuser', password='testpassword'
        )
        self.superuser = get_user_model().objects.create_superuser(
            username='admin', password='adminpassword'
        )
        self.group = Group.objects.create(name='Site Admin')
        self.user.groups.add(self.group)
        self.photo = Photo.objects.create(
            title='Test Photo',
            description='Test Description',
            price=9.99,
            size="8x10 inches",
            is_featured=True,
        )
        self.photo_url = reverse('photo_detail', kwargs={'photo_id': self.photo.id})

    def test_gallery_view(self):
        """Test that the gallery page displays the correct photos."""
        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/gallery.html')
        self.assertContains(response, 'Test Photo')  # Check if photo title is in response
    
    def test_search_view_with_query(self):
        """Test the search view with a valid query."""
        response = self.client.get(reverse('search') + '?q=Test')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Photo')
    
    def test_photo_detail_view(self):
        """Test the photo detail view for a specific photo."""
        response = self.client.get(self.photo_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/photo_detail.html')
        self.assertContains(response, 'Test Photo')
    
    def test_admin_panel_view_superuser(self):
        """Test that a superuser can access the admin panel."""
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('admin_panel'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/admin_panel.html')
        self.assertContains(response, 'Test Photo')

    def test_no_permission_view(self):
        """Test the no permission view."""
        response = self.client.get(reverse('no_permission'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/no_permission.html')
    
    def test_edit_photo_view(self):
        """Test that the edit photo view works correctly for GET requests."""
        self.client.login(username='admin', password='adminpassword')
        response = self.client.get(reverse('edit_photo', kwargs={'photo_id': self.photo.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/edit_photo.html')
        self.assertContains(response, 'Test Photo')
    
    def test_delete_photo_view(self):
        """Test that a photo can be deleted."""
        self.client.login(username='admin', password='adminpassword')
        response = self.client.post(reverse('delete_photo', kwargs={'photo_id': self.photo.id}))
        self.assertRedirects(response, reverse('admin_panel'))
        with self.assertRaises(Photo.DoesNotExist):
            self.photo.refresh_from_db()
    