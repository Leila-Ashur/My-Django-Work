from django.contrib import admin

# Register your models here.
from .models import Accountregistration
class AccountregistrationAdmin(admin.ModelAdmin):
    list_display=("first_name","last_name","email","phone_number","password")
    
admin.site.register(Accountregistration,AccountregistrationAdmin)