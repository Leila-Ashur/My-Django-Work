from django.shortcuts import render, redirect
from .forms import OrderUploadForm
from order.models import Order



def order_upload(request):
    form = OrderUploadForm()
    return render(request, "Order/order_upload.html", {"form": form})


def order_list(request):
    orders = Order.objects.all()
    return render(request, "Order/order_list.html", {"orders": orders})

def order_detail_view(request, id):
    order = Order.objects.get(id=id)  
    return render(request, "Order/order_detail.html", {"order": order})

def edit_order_view(request, id):
    order = Order.objects.get(id=id)
    if request.method == "POST":
        form = OrderUploadForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_detail_view', id=order.id)
    else:
        form = OrderUploadForm(instance=order)
    return render(request, 'edit_order.html', {'form': form})



