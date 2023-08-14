from django.shortcuts import render

# Create your views here.
from .forms import ShoppingcartUploadForm 
from Shoppingcart.models import Shoppingcart
from django.shortcuts import render

def shoppingcart_upload_view(request):
    form = ShoppingcartUploadForm()
    return render(request, "Shoppingcart/Shoppingcart_upload.html", {"form": form})

def shoppingcart_list(request):
    Shoppingcarts = Shoppingcart.objects.all()  
    return render(request, "Shoppingcart/Shoppingcart_list.html", {"Shoppingcarts": Shoppingcarts})

def discount_detail_view(request,id):
    Shoppingcarts=Shoppingcart.objects.get(id=id)
    return render(request,"Discount/Discount_detail_view.html",{"Shoppingcarts":Shoppingcarts})

def edit_Shoppingcart_view(request, id):
   Shoppingcarts = Shoppingcart.objects.get(id=id)
   if request.method == "POST":

    form = ShoppingcartUploadForm(request.POST, instance=Shoppingcarts)
   if form.is_valid():
        form.save()
        return redirect('Shoppingcart_detail_view', id=Shoppingcarts.id)
   else:
    
        form = ShoppingcartUploadForm(instance=Shoppingcart)   
        return render(request, 'edit_Shoppingcart.html', {'form': form})



                 


