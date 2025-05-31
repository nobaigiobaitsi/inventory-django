from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm, UpdateStockForm
from django.contrib import messages
from django.shortcuts import get_object_or_404


def home(request):
    return render(request, "inventory/home.html")


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


def remove_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        product.delete()
        messages.success(request, f"Product '{product.name}' has been deleted.")
        return redirect("product_list")

    return render(request, "inventory/remove_product.html", {"product": product})
