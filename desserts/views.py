from django.shortcuts import render, get_object_or_404, redirect

from .forms import DessertForm
from .models import Dessert
# Create your views here.

def dessert_list(request):
    desserts = Dessert.objects.filter(is_available=True)
    context = {"desserts": desserts}
    return render(request, "desserts/dessert_list.html", context)

def dessert_detail(request, pk):
    dessert = get_object_or_404(Dessert, pk=pk)
    context = {"dessert": dessert}
    return render(request, "desserts/dessert_detail.html", context)

def dessert_create(request):
    if request.method == "POST":
        form = DessertForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("dessert_list")
    else:
        form = DessertForm()

    context = {"form": form}
    return render(request, "desserts/dessert_form.html", context)

def dessert_edit(request, pk):
    dessert = get_object_or_404(Dessert, pk=pk)

    if request.method == "POST":
        form = DessertForm(request.POST, request.FILES, instance=dessert)
        if form.is_valid():
            form.save()
            return redirect("dessert_detail", pk=dessert.pk)
    else:
        form = DessertForm(instance=dessert)

    context = {"form": form, "dessert": dessert}
    return render(request, "desserts/dessert_form.html", context)

def dessert_delete(request, pk):
    dessert = get_object_or_404(Dessert, pk=pk)

    if request.method == "POST":
        dessert.delete()
        return redirect("dessert_list")

    context = {"dessert": dessert}
    return render(request, "desserts/dessert_delete.html", context)