

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from customer.models import Customer
from inventory.models import Product
from order.models import Order
from shoppingcart.models import Shoppingcart

from .serializer import CustomerSerializer
from .serializer import ProductSerializer
from .serializer import OrderSerializer

class CustomerListView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)
    


class CustomerListView(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Corrected status code
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Corrected status code

class CustomerDetailView  (APIView):
    def get(self,request,id,format= None):
        customer=Customer.objects.get(id=id)
        serializer= CustomerSerializer(customer)
        return Response(serializer.data)
        

    def put (self,request,id,format=None):
        customer=Customer.objects.get(id=id)
        serializer=CustomerSerializer(customer,request.data)
        if serializer.is_valid():
            serializer.save()
           
            return Response(serializer.errors,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


        
           


    def Delete(self,request,id,format=None)  :
        customer=Customer.objects.get(id=id)       
        customer.delete()
        return Response ("customer deleted",status=status.HTTP_204_NO_CONTENT)




class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializers = ProductSerializer(product, many=True)
        return Response(serializer.data)
    


class ProductListView(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
class ProductDetailView  (APIView):
    def get(self,request,id,format= None):
        product=Product.objects.get(id=id)
        serializer= ProductSerializer(product)
        return Response(serializer.data)
        

    def put (self,request,id,format=None):
        product=Product.objects.get(id=id)
        serializer=ProductSerializer(product,request.data)
        if serializer.is_valid():
            serializer.save()
           
            return Response(serializer.errors,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


        
           


    def Delete(self,request,id,format=None)  :
        customer=Customer.objects.get(id=id)       
        customer.delete()
        return Response ("customer deleted",status=status.HTTP_204_NO_CONTENT)


               





class OrdertListView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializers = OrderSerializer(order, many=True)
        return Response(serializer.data)
    


class OrderListView(APIView):
    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Corrected status code
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)          



class OrderDetailView  (APIView):
    def get(self,request,id,format= None):
        order=Order.objects.get(id=id)
        serializer= OrderSerializer(order)
        return Response(serializer.data)
        

    def put (self,request,id,format=None):
        order=Order.objects.get(id=id)
        serializer=OrderSerializer(order,request.data)
        if serializer.is_valid():
            serializer.save()
           
            return Response(serializer.errors,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


        
           


    def Delete(self,request,id,format=None)  :
        order=Order.objects.get(id=id)       
        order.delete()
        return Response ("order deleted",status=status.HTTP_204_NO_CONTENT)






class ShoppingcartListView(APIView):
    def get(self, request):
        orders = Shoppingcart.objects.all()
        serializers = ShoppingcartSerializer(order, many=True)
        return Response(serializer.data)
    


class ShoppingcartListView(APIView):
    def post(self, request):
        serializer = ShoppingcartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Corrected status code
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)          



class ShoppingcartDetailView  (APIView):
    def get(self,request,id,format= None):
        shoppingcart=Shoppingcart.objects.get(id=id)
        serializer= ShoppingcartSerializer(order)
        return Response(serializer.data)
        

    def put (self,request,id,format=None):
        Shoppingcart=Shoppingcart.objects.get(id=id)
        serializer=OrderSerializer(order,request.data)
        if serializer.is_valid():
            serializer.save()
           
            return Response(serializer.errors,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


        
           


    def Delete(self,request,id,format=None)  :
        shoppingcart=Shoppingcart.objects.get(id=id)       
        Shoppingcart.delete()
        return Response ("Shoppingcart deleted",status=status.HTTP_204_NO_CONTENT)


