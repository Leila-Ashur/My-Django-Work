from django.contrib import admin
from .models import Orders

# Register your models here.

class OrdersAdmin(admin.ModelAdmin):
    list_display=("Order_status","Customer_information","Item","Amount")
    
admin.site.register(Orders,OrdersAdmin)

