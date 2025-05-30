from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "category", "quantity", "price"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "category": forms.TextInput(attrs={"class": "form-control"}),
            "quantity": forms.NumberInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
        }


class UpdateStockForm(forms.Form):
    product = forms.ModelChoiceField(
        queryset=Product.objects.all(), label="Select Product"
    )
    quantity_change = forms.IntegerField(
        label="Change in Quantity (use negative for removal)"
    )
