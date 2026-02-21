from django.urls import path
from . import views

urlpatterns = [
    path("", views.dessert_list, name="dessert_list"),
    path("<int:pk>/", views.dessert_detail, name="dessert_detail"),
    path("create/", views.dessert_create, name="dessert_create"),
    path("<int:pk>/edit/", views.dessert_edit, name="dessert_edit"),
    path("<int:pk>/delete/", views.dessert_delete, name="dessert_delete"),
]