from django import forms
from WestApp.models import ImageModel

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = "__all__"
