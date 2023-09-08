

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from customer.models import Customer
from inventory.models import Product
from order.models import Order

from .serializer import CustomerSerializer
from .serializer import ProductSerializer
from .serializer import OrderSerializer

class CustomerListView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializers = CustomerSerializer(customer, many=True)
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
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_201_CREATED)

        
           


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





