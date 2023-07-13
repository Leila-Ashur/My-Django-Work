from django.contrib import admin

from .models import Vendor
class Vendor_admin(admin.ModelAdmin):
    list_display = ("name","email","image","phone_number","date_created")
admin.site.register(Vendor,Vendor_admin)

# Register your models here.
