from django.urls import path

from.views import shoppingcart_upload_view,shoppingcart_list,Shoppingcart_detail_view,edit_shoppingcart_view
urlpatterns = [
    path("shoppingcart/upload/",shoppingcart_upload_view,name="shoppingcart_upload_view"),
    path("shoppingcart/list/",shoppingcart_list, name="shoppingcart_list_view") ,
    path ("shoppingcart/<int:id>",Shoppingcart_detail_view,name="shoppingcart_detail_view"),
    path('shoppingcart/edit/<int:id>/', edit_shoppingcart_view, name='edit_shoppingcart_view'),

]
