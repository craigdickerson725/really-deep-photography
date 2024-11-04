import uuid

from django.db import models
from django.db.models import Sum, F
from django.conf import settings

from photos.models import Photo

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def calculate_order_total(self):
        """
        Calculates the total amount by summing all OrderItems' total prices.
        """
        self.order_total = self.items.aggregate(
            total=Sum(F('quantity') * F('price'))
        )['total'] or 0
        self.save()

    def __str__(self):
        return self.order_number

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.photo.title} in Order {self.order.order_number}"

    def get_total_price(self):
        """
        Calculate the total price for this item (quantity * price).
        """
        return self.quantity * self.price

    def save(self, *args, **kwargs):
        """
        Override the save method to ensure the price is set correctly
        and the order total is updated when an OrderItem is saved.
        """
        # Optionally, set price from the current photo price if it's not already set
        if not self.price:
            self.price = self.photo.price  # Assuming `photo.price` exists

        # Save the OrderItem instance
        super().save(*args, **kwargs)

        # Update the order total
        self.order.calculate_order_total()