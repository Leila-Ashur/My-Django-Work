from django.db import models
from customer.models import Customer
from Delivery.models import Delivery
from Shoppingcart.models import Shoppingcart

# Create your models here.
class Orders (models.Model):
   Order_status=models.CharField(max_length=32)
   Item=models.CharField(max_length=32)
   Customer_information=models.CharField(max_length=15)
   Amount=models.DecimalField(max_digits=7,decimal_places=3)

def __str__(self) :
    return self.name
    customer =models.ForeignKey(Customer,null=True,on_delete=models.CASCADE)
    delivery= models.OneToOneField(Delivery,null=True, on_delete=models.CASCADE)
    shoppingcart =models.ManyToManyField(Shoppingcart)


    


