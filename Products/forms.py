from django import forms

from .models import Category

class FormCategory(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name','url_img')
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style': 'flex : 1 0 10rem;', 'placeholder':'Nombre'}))
    url_img = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style': 'flex : 1 0 10rem;', 'placeholder':'URL de la imagen'}))