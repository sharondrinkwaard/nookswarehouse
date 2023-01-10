from django import forms
from .models import QuantitySize


class ShoppingcartForm(forms.ModelForm):
    class Meta:
        model = QuantitySize
        # Excluding the color option for now
        # Needing it to continue after this project
        exclude = ('color_option',)
