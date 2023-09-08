from rest_framework import serializers
from customer.models import Customer
from inventory.models import Product
from order.models import Order
from shoppingcart.models import Shoppingcart



class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        models=Customer
        fields= "__all__"
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        models=Product
        fields= "__all__"
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        models=Order
        fields= "__all__"

class ShoppingcartSerializer(serializers.ModelSerializer):
    class Meta:
        models=Shoppingcart
        fields= "__all__"

