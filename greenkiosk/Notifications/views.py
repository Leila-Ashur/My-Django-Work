
from django.shortcuts import render, get_object_or_404
from .forms import NotificationsUploadForm
from .models import Notifications 

def Notifications_upload_view(request):
    form = NotificationsUploadForm()
    return render(request, "Notifications/Notifications_upload.html", {"form": form})

def Notifications_list(request):
    notifications = Notifications.objects.all()
    return render(request, "Notifications/Notifications_list.html", {"notifications": notifications})

def Notifications_detail_view(request, id):
    notifications = get(id=id)
    return render(request, "Notifications/Notifications_detail_view.html", {"notifications": notifications})


def edit_Notifications_view(request, id):
    notifications = Notifications.objects.get(id=id)
    if request.method == "POST":
        form = NotificationsUploadForm(request.POST, instance=notifications)  
        if form.is_valid():
            form.save()
            return redirect('Notifications_detail_view', id=notifications)
    else:
        form = NotificationsUploadForm(instance=notifications)  
        return render(request, 'edit_Notifications.html', {'form': form})
