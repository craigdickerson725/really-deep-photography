from django.db import models
from django.contrib.auth.models import User

# Photo Model
class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/')
    size = models.CharField(max_length=50, default="8x10 inches")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def price_display(self):
        return f"${self.price:.2f}"

    def __str__(self):
        return self.title

# Cart Model
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f"{self.user.username}'s Cart"

# CartItem Model
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        """Calculate the total price of this cart item."""
        return self.photo.price * self.quantity

    def __str__(self):
        return f"{self.quantity} of {self.photo.title} in {self.cart.user.username}'s Cart"
