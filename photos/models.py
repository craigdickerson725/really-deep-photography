from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Photo Model
class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = CloudinaryField('image')  # Store image on Cloudinary
    size = models.CharField(max_length=50, default="8x10 inches")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_featured = models.BooleanField(default=False)  # Featured flag

    @property
    def price_display(self):
        """Display the price formatted as a string."""
        return f"${self.price:.2f}"

    def __str__(self):
        return self.title
