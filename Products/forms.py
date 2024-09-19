from django import forms

from .models import Category, Product

class FormCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name','url_img')
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style': 'flex : 1 0 10rem;', 'placeholder':'Nombre'}))
    url_img = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style': 'flex : 1 0 10rem;', 'placeholder':'URL de la imagen'}))

from django import forms
from .models import Product, Category

class FormProduct(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'price', 'count', 'url_img')
    
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'flex : 1 0 10rem;',
            'placeholder': 'Nombre'
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Descripción',
            'rows': 3
        })
    )
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )
    price = forms.DecimalField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Precio'
        })
    )
    count = forms.IntegerField(
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Cantidad'
        })
    )
    url_img = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'style': 'flex : 1 0 10rem;',
            'placeholder': 'URL de la imagen'
        })
    )
