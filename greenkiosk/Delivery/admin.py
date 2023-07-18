from django.contrib import admin
from .models import Delivery
# Register your models here.
class DeliveryAdmin(admin.ModelAdmin):
    list_display=("name","date","time","address","is_delivered")
admin.site.register(Delivery,DeliveryAdmin)



