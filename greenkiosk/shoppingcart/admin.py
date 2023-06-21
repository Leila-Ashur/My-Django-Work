from django.contrib import admin

# Register your models here.
from.models import Shopping

class ShoppingAdmin(admin.ModelAdmin):
    list_display=("name","quantity","price","total_price")
    
admin.site.register(Shopping,ShoppingAdmin)

