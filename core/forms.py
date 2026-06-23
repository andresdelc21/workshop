from django import forms

from .models import Product


class ContactoForm(forms.Form):
    email = forms.EmailField(label='Correo electronico')

    def clean_email(self):
        email = self.cleaned_data['email']

        if not email.endswith('@example.com'):
            raise forms.ValidationError('El correo debe ser de dominio example.com')

        return email



class LibroInlineForm(forms.ModelForm):
    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo', '')

        if titulo and 'django' not in titulo.lower():
            raise forms.ValidationError('El titulo debe contener la palabra "Django".')

        return titulo

    def clean(self):
        cleaned_data = super().clean()
        fecha_publicacion = cleaned_data.get('fecha_publicacion')

        if fecha_publicacion and fecha_publicacion.year < 2000:
            raise forms.ValidationError('La fecha de publicacion debe ser posterior al año 2000.')

        return cleaned_data



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'description', 'available']


class ProductSearchForm(forms.Form):
    q = forms.CharField(label='Buscar producto', required=False)
    category = forms.CharField(label='Categoria', required=False)
