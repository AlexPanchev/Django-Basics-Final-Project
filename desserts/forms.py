from django import forms

from desserts.models import Dessert, Category


class DessertForm(forms.ModelForm):
    class Meta:
        model = Dessert
        fields = '__all__'

        labels = {
            "name": "Dessert Name",
            "description": "Dessert Description",
            "price": "Dessert Price",
            "image": "Dessert Image",
            "category": "Dessert Category",
            "ingredients": "Ingredients Used",
        }

        widgets = {
            "description": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Please enter Dessert Description",
            }),
        }

        error_messages = {
            "name": {
                "required": "Please enter a dessert name.",
                "max_length": "Dessert name cannot exceed 100 characters.",
            },
            "price": {
                "required": "Please enter a dessert price.",
                "min_value": "Price can't be a negative number",
            },
            "image": {
                "invalid": "Please upload a valid image file.",
            }
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    labels = {
        "name": "Category Name",
        "description": "Category Description",
    }

    widgets = {
        "description": forms.Textarea(attrs={"rows": 3}),
    }

    error_messages = {
        "name": {
            "required": "Please enter a category name.",
        }
    }