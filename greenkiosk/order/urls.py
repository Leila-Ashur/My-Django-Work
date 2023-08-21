from django.urls import path
from.views import order_detail_view,order_upload,order_list,edit_order_view

urlpatterns=[
   
    path("order/list/",order_list, name="order_list") ,
    path ("order/<int:id>",order_detail_view,name="order_detail_view"),
    path('order/edit/<int:id>/', edit_order_view, name='edit_order_view'),
    path('order/upload/', order_upload, name='order_upload'),

]
