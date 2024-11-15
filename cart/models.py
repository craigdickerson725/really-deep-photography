from django.db import models
from django.contrib.auth.models import User
from photos.models import Photo


# Cart Model
class Cart(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='cart'
    )

    def get_total(self):
        return sum(item.subtotal for item in self.items.all())

    def __str__(self):
        return f"{self.user.username}'s Cart"


# CartItem Model
class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, related_name='items'
        )
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def subtotal(self):
        return self.photo.price * self.quantity

    def __str__(self):
        return f"{self.quantity} of {self.photo.title} in {self.cart.user.username}'s Cart"  # noqa
