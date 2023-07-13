from django.contrib import admin
from .models import Customer
# Register your models here.

class Customer_admin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email","phone","password")
admin.site.register(Customer,Customer_admin)


