from django.contrib import admin
from .models import Photo, Cart, CartItem, Order, OrderItem

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'is_featured')
    # Add search capability for these fields
    search_fields = ('title', 'description')

class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    # Allow searching by username
    search_fields = ('user__username',)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'photo', 'quantity', 'subtotal')
    # Allow searching by cart owner or photo title
    search_fields = ('cart__user__username', 'photo__title')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'total_amount', 'payment_intent_id')
    # Allow searching by username or payment intent ID
    search_fields = ('user__username', 'payment_intent_id')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'photo', 'quantity', 'subtotal')
    # Allow searching by order ID or photo title
    search_fields = ('order__id', 'photo__title')

# Register your models with the admin site
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
