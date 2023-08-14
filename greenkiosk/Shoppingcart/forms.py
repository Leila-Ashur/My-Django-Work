from django import forms
from .models import Shoppingcart
class ShoppingcartUploadForm(forms.ModelForm):
    class Meta:
        model= Shoppingcart
        fields= "__all__"