from .forms import ShoppingcartUploadForm
from shoppingcart.models import Shoppingcart
from django.shortcuts import render

def shoppingcart_upload_view(request):
    form = ShoppingcartUploadForm()
    return render(request, "shoppingcart/shoppingcart_upload.html", {"form": form})

def shoppingcart_list(request):
    shoppingcart = Shoppingcart.objects.all()  
    return render(request, "shoppingcart/shoppingcart_list.html", {"shoppingcart": shoppingcart})

def Shoppingcart_detail_view(request,id):
    shoppingcart=Shoppingcart.objects.get(id=id)
    return render(request,"shoppingcart/shoppingcart_detail_view.html",{"shoppingcart":shoppingcart})

def edit_shoppingcart_view(request, id):
    shoppingcart = Shoppingcart.objects.get(id=id)
    
    if request.method == "POST":
        form = ShoppingcartUploadForm(request.POST, instance=shoppingcart)
        if form.is_valid():
            form.save()
            return redirect('shoppingcart_detail_view', id=shoppingcart.id)
    else:
        form = ShoppingcartUploadForm(instance=shoppingcart)   
        
    return render(request, 'shoppingcart/edit_shoppingcart.html', {'form': form})

                 


