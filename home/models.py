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

# Cart Model
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

    def get_total(self):
        """Calculate the total cost of all items in the cart."""
        return sum(item.subtotal for item in self.items.all())

    def __str__(self):
        return f"{self.user.username}'s Cart"

# CartItem Model
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def subtotal(self):
        """Calculate the subtotal for this cart item."""
        return self.photo.price * self.quantity

    def __str__(self):
        return f"{self.quantity} of {self.photo.title} in {self.cart.user.username}'s Cart"

# Order Model
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    billing_name = models.CharField(max_length=255)
    billing_address_1 = models.CharField(max_length=255)
    billing_city = models.CharField(max_length=100)
    billing_state = models.CharField(max_length=100)
    billing_zip_code = models.CharField(max_length=20)
    billing_country = models.CharField(max_length=100)
    shipping_address_1 = models.CharField(max_length=255, blank=True, null=True)
    shipping_city = models.CharField(max_length=100, blank=True, null=True)
    shipping_state = models.CharField(max_length=100, blank=True, null=True)
    shipping_zip_code = models.CharField(max_length=20, blank=True, null=True)
    shipping_country = models.CharField(max_length=100, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def calculate_total(self):
        """Calculate and save the total amount based on OrderItems."""
        total = sum(item.subtotal for item in self.items.all())
        self.total_amount = total
        self.save()

    def __str__(self):
        return f"Order {self.id} by {self.user}"

# OrderItem Model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        """Automatically set the subtotal based on quantity and photo price."""
        self.subtotal = self.photo.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity} of {self.photo.title}"
