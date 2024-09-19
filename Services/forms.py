from django import forms

from .models import Service

class FormService(forms.ModelForm):
    class Meta:
        model = Service
        fields = ('name','description','url_img')
    
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style': 'flex : 1 0 10rem;', 'placeholder':'Nombre'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','style': 'flex : 1 0 10rem;', 'placeholder':'Descripcion'}))
    url_img = forms.URLField(widget=forms.TextInput(attrs={'class':'form-control','style': 'flex : 1 0 10rem;', 'placeholder':'URL de la imagen'}))