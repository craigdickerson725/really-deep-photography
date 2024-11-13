from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from django.contrib.auth.models import AnonymousUser
from photos.models import Photo

class HomeViewTests(TestCase):
    def setUp(self):
        # Define featured photos with price
        self.featured_photo1 = Photo.objects.create(
            title="Featured Photo 1", is_featured=True, price=10.00
        )
        self.featured_photo2 = Photo.objects.create(
            title="Featured Photo 2", is_featured=True, price=15.00
        )
        self.featured_photo3 = Photo.objects.create(
            title="Featured Photo 3", is_featured=True, price=20.00
        )
        
        # Define a non-featured photo for testing
        self.non_featured_photo = Photo.objects.create(
            title="Non-Featured Photo", is_featured=False, price=5.00
        )

    def test_index_view_renders_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_index_view_featured_photos_display(self):
        response = self.client.get(reverse('home'))
        featured_photos = response.context['featured_photos']
        self.assertEqual(len(featured_photos), 3)
        self.assertIn(self.featured_photo1, featured_photos)
        self.assertIn(self.featured_photo2, featured_photos)
        self.assertIn(self.featured_photo3, featured_photos)
        self.assertNotIn(self.non_featured_photo, featured_photos)

    def test_index_view_message_filtering(self):
        # Your test setup goes here
        response = self.client.get(reverse('home'))

        # Get messages
        messages = list(get_messages(response.wsgi_request))  # Use get_messages with request here

        # Now you can check the messages
        for msg in messages:
            self.assertNotIn('Added', msg.message)
            self.assertNotIn('Updated', msg.message)

        # Additional assertions
        self.assertEqual(response.status_code, 200)
