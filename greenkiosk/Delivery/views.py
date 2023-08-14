from .forms import DeliveryUploadForm 
from Delivery.models import Delivery
from django.shortcuts import render

def Delivery_upload_view(request):
    form = DeliveryUploadForm()
    return render(request, "Delivery/Delivery_upload.html", {"form": form})

def Delivery_list(request):
    Delivery = Delivery.objects.all() 
    return render(request, "Delivery/Delivery_list.html", {"Delivery": Delivery})

def Delivery_detail_view(request,id):
    Delivery=Delivery.objects.get(id=id)
    return render(request,"Delivery/Delivery_detail_view.html",{"Delivery":Delivery})


# def edit_product_view(request, id):
#     product = Product.objects.get(id=id)
#     if request.method == "POST":
#         form = ProductUploadForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('product_detail_view', id=product.id)
#     else:
#         form = ProductUploadForm(instance=product)   
#     return render(request, 'edit_product.html', {'form': form})



                 

