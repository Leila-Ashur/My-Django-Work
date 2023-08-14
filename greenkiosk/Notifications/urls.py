from django.urls import path
from.views import Notifications_upload_view,Notifications_list,Notifications_detail_view,edit_Notifications_view

urlpatterns=[
    path("Notifications/upload/",Notifications_upload_view,name="Notifications_upload_view"),
    path("Notifications/list/",Notifications_list, name="Notifications_list") ,
    path ("Notifications/<int:id>",Notifications_detail_view,name="Notifications_detail_view"),
    path('Notifications/edit/<int:id>/', edit_Notifications_view, name='edit_Notifications_view'),

]
