from django.db import models

class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/')
    size = models.TextField(default="8x10 inches")
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def price_display(self):
        return "$%s" % self.price

    def __str__(self):
        return self.title
