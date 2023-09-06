from django.shortcuts import render
from .forms import ProductUploadForm
from inventory.models import Product
from django.shortcuts import redirect
# from inventory.views import product_upload_view

# Create your views here.
def product_upload(request):
    request.method == 'POST'
    form =ProductUploadForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return render(request,"inventory/product_upload.html",{"form":form})

def product_list(request):
    products = Product.objects.all()
    return render(request,"inventory/product_list.html",{"products":products})

def product_detail_view(request,id):
    product=Product.objects.all()
    return render(request,"inventory/product_detail.html",{"products":product})


def edit_product_view(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductUploadForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_detail_view', id=product.id)
        else:
            form = ProductUploadForm(instance=product)
            return render(request,'edit_product.html', {'form': form})



                 
