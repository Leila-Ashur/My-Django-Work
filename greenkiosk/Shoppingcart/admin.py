from django.contrib import admin
from .models import Shoppingcart


# Register your models here.

class ShoppingAdmin(admin.ModelAdmin):
    list_display=("name","quantity","price","total_price")
    
admin.site.register(Shoppingcart,ShoppingAdmin)


