from django.contrib import admin

# Register your models here.
from .models import Orders
class OrdersAdmin(admin.ModelAdmin):
    list_display=("Order_status","Customer_information","Item","Amount")
    
admin.site.register(Orders,OrdersAdmin)

