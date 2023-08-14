from .models import Accountregistration 
from .forms import AccountregistrationUploadForm 
from django.shortcuts import render

def Accountregistration_upload_view(request):
    form = AccountregistrationUploadForm()
    return render(request, "Accountregistration/Accountregistration_upload.html", {"form": form})

def Accountregistration_list(request):
    account_registrations = Accountregistration.objects.all() 
    return render(request, "Accountregistration/Accountregistration_list.html", {"account_registrations": account_registrations})



def Accountregistration_detail_view(request,id):
    Accountregistration=Accountregistration.objects.get(id=id)
    return render(request,"Accountregistration/Accountregistration_detail_view.html",{"Accountregistration":Accountregistration})


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



                 

