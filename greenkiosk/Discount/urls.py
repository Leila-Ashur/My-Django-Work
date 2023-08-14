from django.urls import path
from.views import Discount_upload_view,Discount_list,Discount_detail_view,edit_Discount_view

urlpatterns=[
    path("Discount/upload/",Discount_upload_view,name="Discount_upload_view"),
    path("Discount/list/",Discount_list, name="customer_list") ,
    path ("Discount/<int:id>",Discount_detail_view,name="Discount_detail_view"),
    path('Discount/edit/<int:id>/', edit_Discount_view, name='edit_Discount_view'),

]
