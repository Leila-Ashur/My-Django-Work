from django.urls import path
from .views import shoppingcart_list, shoppingcart_upload_view, shoppingcart_detail_view, edit_shoppingcart_view

urlpatterns = [
    path("shoppingcart/upload/",shoppingcart_upload_view,name="Shoppingcart_upload_view"),
    path("shoppingcart/list/",shoppingcart_list, name="shoppingcart_list") ,
    path ("shoppingcart/<int:id>",shoppingcart_detail_view,name="shoppingcart_detail_view"),
    path('shoppingcart/edit/<int:id>/', edit_shoppingcart_view, name='edit_shoppingcart_view'),

]
