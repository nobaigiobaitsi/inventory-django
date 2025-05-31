from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("products/", views.product_list, name="product_list"),
    path("add/", views.add_product, name="add_product"),
    path("base/", views.base_page, name="base"),
    path("update/", views.update_product_stock, name="update_product_stock"),
    path("remove/<int:product_id>/", views.remove_product, name="remove_product"),
    path("remove/", views.remove_product_select, name="remove_product_select"),
]
