from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm, UpdateStockForm
from django.contrib import messages


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


def update_product_stock(request):
    if request.method == "POST":
        form = UpdateStockForm(request.POST)
        if form.is_valid():
            product = form.cleaned_data["product"]
            quantity_change = form.cleaned_data["quantity_change"]
            new_stock = product.quantity + quantity_change

            if new_stock < 0:
                messages.error(
                    request,
                    f"Cannot reduce stock below zero. Current stock: {product.quantity}",
                )
            else:
                product.quantity = new_stock
                product.save()
                messages.success(
                    request,
                    f"Stock updated. New stock for {product.name}: {product.quantity}",
                )
                return redirect("product_list")
    else:
        form = UpdateStockForm()

    return render(request, "inventory/update_stock.html", {"form": form})
