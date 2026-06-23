from django import forms



class BusquedaUsuarioForm(forms.Form):
    q = forms.CharField(label='Buscar usuario', required=False)
