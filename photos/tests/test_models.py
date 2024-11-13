from django.test import TestCase
from photos.models import Photo
from decimal import Decimal


class PhotoModelTests(TestCase):

    def setUp(self):
        """Set up a sample Photo object for testing."""
        self.photo = Photo.objects.create(
            title="Sample Photo",
            description="A beautiful landscape",
            image="sample_image.jpg",
            size="8x10 inches",
            price=Decimal("25.00"),
            is_featured=True
        )

    def test_photo_creation(self):
        """Test that a Photo object is created correctly."""
        photo = self.photo
        self.assertEqual(photo.title, "Sample Photo")
        self.assertEqual(photo.description, "A beautiful landscape")
        self.assertEqual(photo.size, "8x10 inches")
        self.assertEqual(photo.price, Decimal("25.00"))
        self.assertTrue(photo.is_featured)

    def test_price_display(self):
        """Test the price_display method formats the price correctly."""
        photo = self.photo
        self.assertEqual(photo.price_display, "$25.00")

    def test_photo_str(self):
        """Test the __str__ method returns the correct title."""
        photo = self.photo
        self.assertEqual(str(photo), "Sample Photo")