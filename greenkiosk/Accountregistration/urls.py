from django.urls import path
from.views import Accountregistration_upload_view,Accountregistration_list,Accountregistration_detail_view
urlpatterns=[
    path("Accountregistration/upload/",Accountregistration_upload_view,name="Accountregistration_upload_view"),
    path("Accountregistration/list/",Accountregistration_list, name="Accountregistration_list") ,
    path ("Accountregistration/<int:id>",Accountregistration_detail_view,name="Accountregistration_detail_view"),
    # path('/products/edit/<int:id>/', edit_product_view, name='edit_product_view'),

]
