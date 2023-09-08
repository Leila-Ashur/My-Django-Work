
from django.shortcuts import render
from .forms import CommentsUploadForm
from review.models import Comments
from django.shortcuts import redirect
# from inventory.views import product_upload_view

# Create your views here.
def comments_upload(request):
    request.method == 'POST'
    form =CommentsUploadForm(request.POST,request.FILES)
    if form.is_valid():
        form.save()
        return render(request,"review/comments_upload.html",{"form":form})

def comments_list(request):
    comments = Comments.objects.all()
    return render(request,"review/comments_list.html",{"comments":comments})

def comments_detail_view(request,id):
    comments=Comments.objects.all()
    return render(request,"review/comments_detail.html",{"comment":comments})


def edit_comments_view(request, id):
    comments = Comments.objects.get(id=id)
    if request.method == "POST":
        form = ProductUploadForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('comments_detail_view', id=product.id)
        else:
            form = CommentsUploadForm(instance=comments)
            return render(request,'edit_comments.html', {'form': form})



                 
