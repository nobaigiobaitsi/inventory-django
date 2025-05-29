from .models import Product
from django.core.exceptions import ValidationError

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

    product = Product(
        name=name,
        category=category,
        quantity=quantity,
        price=price
    )
    product.save()

    return f"Product '{name}' added successfully."


# Update the stock of an existing product
