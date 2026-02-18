from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    is_allergen = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Dessert(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='desserts/', blank=True, null=True)
    is_available = models.BooleanField(default=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='desserts'
    )

    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='desserts',
        blank=True
    )

    def __str__(self):
        return self.name