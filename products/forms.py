from django import forms
from .models import QuantitySize, Product


class ProductSize(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('size_option',)


class ProductQuantity(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('quantity',)


class ProductColor(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('color_option',)
