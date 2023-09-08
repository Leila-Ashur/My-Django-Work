from django import forms
from .models import Comments
class CommentsUploadForm(forms.ModelForm):
    class Meta:
        model= Comments
        fields= "__all__"