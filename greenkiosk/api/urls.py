

from django.urls import path
from .views import CustomerListView
from .views import CustomerDetailView
from .views import ProductListView
from .views import OrderListView

from .views import ShoppingcartListView


urlpatterns = [
    path("customers", CustomerListView.as_view(), name="customer_list_view"),
    path ("customers/<int:id>/", CustomerDetailView.as_view(),name="customer_detail_view"),
    path("products/", ProductListView.as_view(), name="product_list_view"),
    path("orders/", OrderListView.as_view(), name="orders_list_view"),
    path("shoppingcarts/", ShoppingcartListView.as_view(), name="shoppingcarts_list_view"),



]
