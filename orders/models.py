from django.core.validators import MinValueValidator
from django.db import models

from desserts.models import Dessert


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = 'Pending', 'Pending'
        COMPLETED = 'Completed', 'Completed'
        CONFIRMED = 'Confirmed', 'Confirmed'


    customer_name = models.CharField(
        max_length=100,
        verbose_name='Customer Name',
        )
    customer_phone = models.CharField(
        max_length=100,
        help_text='Enter a valid phone number',
    )
    customer_email = models.EmailField(
        verbose_name='Customer Email'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(
        blank=True,
        help_text='Optional notes for the order',
    )
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.PENDING,
        verbose_name='Order Status',
    )

    def __str__(self):
        return f"{self.customer_name} ({self.status})"

    def total_price(self):
        return sum(item.line_total() for item in self.items.all())

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Orders"
        ordering = ["-created_at"]

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    dessert = models.ForeignKey(Dessert, on_delete=models.CASCADE, related_name='order_items')

    quantity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Quantity",
        help_text="Enter the number of items.",
    )

    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)],
    )

    def __str__(self):
        return f"{self.quantity}x {self.dessert}"

    def line_total(self):
        return self.unit_price * self.quantity

    class Meta:
        ordering = ["order"]
