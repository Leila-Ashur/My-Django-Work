from django.urls import path
from .views import comments_detail_view,comments_upload,comments_list,edit_comments_view
from .views import comments_detail_view

urlpatterns=[
    path("comments/upload/",comments_upload,name="comments_upload_view"),
    path("comments/list/",comments_list, name="comments_list_view") ,
    path ("comments/<int:id>/",comments_detail_view,name="comments_detail_view"),
    path('comments/edit/<int:id>/', edit_comments_view, name='edit_comments_view'),

]
