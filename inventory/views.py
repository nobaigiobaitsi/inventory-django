from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm


def base_page(request):
    return render(request, "inventory/base.html")


def product_list(request):
    products = Product.objects.all()
    return render(request, "inventory/product_list.html", {"products": products})


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product_list")
    else:
        form = ProductForm()

    return render(request, "inventory/add_product.html", {"form": form})
