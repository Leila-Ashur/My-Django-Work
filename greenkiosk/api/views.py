

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from customer.models import Customer
from .serializer import CustomerSerializer

class CustomerListView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializers = CustomerSerializer(customers, many=True)
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
        serialiser= CustomerSerializer(customer)
        return Response(serialiser.data)
        

    def put (self,request,id,format=None):
        customer=Customer.objects.get(id=id)
        serialiser=CustomerSerializer(customer,request.data)
        if serialiser.is_valid():
            serialiser.save()
            return Response(serialiser.data)
        return Response(serialiser.errors,status=status.HTTP_201_CREATED)   


    def Delete(self,request,id,format=None)  :
        customer=Customer.objects.get(id=id)       
        customer.delete()
        return Response ("customer deleted",status=status.HTTP_204_NO_CONTENT)





