from django.contrib import admin

# Register your models here.
from .models import Shoppingcart

class ShoppingAdmin(admin.ModelAdmin):
    list_display=("name","quantity","price","total_price")
    
admin.site.register(Shoppingcart,ShoppingAdmin)

