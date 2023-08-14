from django.urls import path
from.views import Delivery_upload_view,Delivery_list,Delivery_detail_view
urlpatterns=[
    path("Delivery/upload/",Delivery_upload_view,name="Delivery_upload_view"),
    path("Delivery/list/",Delivery_list, name="Delivery_list") ,
    path ("Delivery/<int:id>",Delivery_detail_view,name="Delivery_detail_view"),
    # path('/products/edit/<int:id>/', edit_product_view, name='edit_product_view'),

]
