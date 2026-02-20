from django.contrib import admin

from desserts.models import Category, Ingredient, Dessert


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
    ordering = ("name",)

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ("name", "is_allergen")
    search_fields = ("name",)
    ordering = ("name",)

@admin.register(Dessert)
class DessertAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "category", "is_available")
    list_filter = ("category", "is_available")
    search_fields = ("name", "category__name")
    ordering = ("name",)

