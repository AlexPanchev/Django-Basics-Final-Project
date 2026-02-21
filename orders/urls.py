from . import views
from django.urls import path

urlpatterns = [
    path("", views.order_list, name="order_list"),
    path("create/", views.order_create, name="order_create"),
    path("<int:pk>/", views.order_detail, name="order_detail"),
    path("<int:order_pk>/add-item/", views.orderitem_create, name="orderitem_create"),
    path("<int:pk>/delete/", views.order_delete, name="order_delete"),
    path("item/<int:pk>/delete/", views.orderitem_delete, name="orderitem_delete"),
    path("<int:pk>/edit/", views.order_update, name="order_update"),
    path("item/<int:pk>/edit/", views.orderitem_update, name="orderitem_update"),
]