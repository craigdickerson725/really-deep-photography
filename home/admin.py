from django.contrib import admin
from .models import Order, OrderItem

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'billing_name', 'total_amount', 'payment_intent_id')
    search_fields = ('user__username', 'payment_intent_id')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'photo', 'quantity', 'subtotal')
    search_fields = ('order__id', 'photo__title')

# Register your models with the admin site
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
