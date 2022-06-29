from django import forms

from .models import SketchImage


class ImageForm(forms.ModelForm):
    """Form for the image model"""

    class Meta:
        model = SketchImage
        fields = ('image',)
