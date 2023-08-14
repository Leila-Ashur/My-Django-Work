from django.urls import path
from.views import product_detail_view,product_upload,product_list,edit_product_view

urlpatterns=[
    path("products/upload/",product_upload,name="product_upload_view"),
    path("products/list/",product_list, name="product_list_view") ,
    path ("products/<int:id>/",product_detail_view,name="product_detail_view"),
    path('/products/edit/<int:id>/', edit_product_view, name='edit_product_view'),

]
