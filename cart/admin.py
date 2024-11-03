from django.contrib import admin
from .models import Cart, CartItem

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ('user__username',)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'photo', 'quantity', 'subtotal')
    search_fields = ('cart__user__username', 'photo__title')

# Register the cart-related models with the admin site
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
