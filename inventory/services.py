from .models import Product
from django.core.exceptions import ValidationError, ObjectDoesNotExist


# Add a new product to the inventory
def add_product(name: str, category: str, quantity: int, price: float) -> str:
    if not name.strip():
        raise ValidationError("Product name cannot be empty.")
    if quantity < 0:
        raise ValidationError("Quantity cannot be negative.")
    if price <= 0:
        raise ValidationError("Price must be greater than zero.")

    if Product.objects.filter(name=name).exists():
        raise ValidationError(f"A product with the name '{name}' already exists.")

    product = Product(name=name, category=category, quantity=quantity, price=price)
    product.save()

    return f"Product '{name}' added successfully."


# Update the stock of an existing product
def update_product_stock(product_id: int, delta: int) -> str:
    if delta == 0:
        raise ValidationError("Delta must not be zero.")
    if product_id <= 0:
        raise ValidationError("Product ID must be a positive integer.")

    try:
        product = Product.objects.get(id=product_id)
    except ObjectDoesNotExist:
        raise ValidationError(f"No product found with ID {product_id}.")

    new_quantity = product.quantity + delta
    if new_quantity < 0:
        raise ValidationError(
            f"Cannot reduce stock below zero. Current: {product.quantity}, attempted change: {delta}."
        )

    product.quantity = new_quantity
    product.save()
    return f"Stock updated. New quantity: {product.quantity}"


# Remove a product from the inventory
def remove_product(product_id: int) -> str:
    if product_id <= 0:
        raise ValidationError("Product ID must be a positive integer.")

    try:
        product = Product.objects.get(id=product_id)
    except ObjectDoesNotExist:
        raise ValidationError(f"No product found with ID {product_id}.")

    product.delete()
    return f"Product with ID {product_id} removed successfully."


# Returns a list of all products in the inventory
"""
def get_inventory():
    return list(Product.objects.all())

This is now obsolete as the product_list view in views.py handles this.
I just keep it to remember my logic.
"""
