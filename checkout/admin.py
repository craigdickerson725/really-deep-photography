from django.contrib import admin
from .models import Order, OrderItem

class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('photo', 'quantity', 'price', 'get_total_price')
    extra = 0  # Prevents extra empty rows from appearing

    def get_total_price(self, obj):
        return obj.get_total_price()
    get_total_price.short_description = 'Total Price'

class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderItemAdminInline,)

    readonly_fields = ('order_number', 'date', 'order_total')

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'order_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'order_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)
