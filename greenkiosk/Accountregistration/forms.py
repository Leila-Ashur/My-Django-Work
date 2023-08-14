from django import forms
from .models import Accountregistration
class AccountregistrationUploadForm(forms.ModelForm):
    class Meta:
        model= Accountregistration
        fields= "__all__"