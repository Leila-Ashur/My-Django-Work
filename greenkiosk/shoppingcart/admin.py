from django.contrib import admin
from .models import Shoppingcart


# Register your models here.

class ShoppingcartAdmin(admin.ModelAdmin):
    list_display=("name","quantity","price","total_price","image")
    
admin.site.register(Shoppingcart,ShoppingcartAdmin)


