from django import forms
from django.db import models
from django.db.models import fields
from .models import *

class inputTipoProducto(forms.ModelForm):
    class Meta:
        model = TipoProducto
        fields = ['nombre']

class inputProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock', 'desc', 'idTipoProducto']

class inputTipoServicio(forms.ModelForm):
    class Meta:
        model = TipoServicio
        fields = ['nombre']

class inputServicio(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = '__all__'

class inputCliente(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class inputMoto(forms.ModelForm):
    class Meta:
        model = Moto
        fields = '__all__'
