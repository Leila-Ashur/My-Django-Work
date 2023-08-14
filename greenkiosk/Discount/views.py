from .forms import DiscountUploadForm 
from Discount.models import Discount
from django.shortcuts import render

def Discount_upload_view(request):
    form = DiscountUploadForm()
    return render(request, "Discount/Discount_upload.html", {"form": form})

def Discount_list(request):
    discounts = Discount.objects.all()  
    return render(request, "Discount/Discount_list.html", {"discounts": discounts})

def Discount_detail_view(request,id):
    discounts=Discount.objects.get(id=id)
    return render(request,"Discount/Discount_detail_view.html",{"discounts":discounts})

def edit_Discount_view(request, id):
   discounts = Discount.objects.get(id=id)
   if request.method == "POST":

    form = DiscountUploadForm(request.POST, instance=Discount)
   if form.is_valid():
        form.save()
        return redirect('Discount_detail_view', id=Discount.id)
   else:
    
        form = DiscountUploadForm(instance=Discount)   
        return render(request, 'edit_Discount.html', {'form': form})



                 


