from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.product_list, name="product_list"),
    path("add/", views.add_product, name="add_product"),
    path("base/", views.base_page, name="base"),
]
