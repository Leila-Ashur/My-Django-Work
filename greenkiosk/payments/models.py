from django.db import models

# Create your models here.
class Payments (models.Model):
   Payments_status=models.CharField(max_length=32)
   Transation_ID=models.CharField(max_length=10)
   Payment_method=models.CharField(max_length=15)
 


    
def __str__(self) :
    return self.name