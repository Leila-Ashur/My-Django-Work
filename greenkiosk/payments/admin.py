from django.contrib import admin

# Register your models here.
from .models import Payments
class PaymentsAdmin(admin.ModelAdmin):
    list_display=()
    
admin.site.register(Payments,PaymentsAdmin)

