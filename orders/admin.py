from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.




@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_phone', 'customer_email', 'created_at', 'status', "total_price_display",)
    search_fields = ('customer_name', 'customer_email')
    list_filter = ('status',)

    def total_price_display(self, obj):
        return obj.total_price()


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'dessert', 'quantity','unit_price')
    search_fields = ('order__customer_name',)