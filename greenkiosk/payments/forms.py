from django import forms
from .models import Product
class ProductUploadForm(forms.ModelForm):
    class Meta:
        model= payments
        fields= "__all__"de