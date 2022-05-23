from logging import PlaceHolder
from datetime import datetime
from tkinter import Widget
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
        fields = ['nombre', 'precio', 'stock', 'desc', 'idTipoProducto', 'imagen']
    def __init__(self, *args, **kwargs):
        super(inputProducto, self).__init__(*args, **kwargs)
        self.fields['stock'].label = 'Unidades Disponibles'
        self.fields['desc'].label = 'Descripción'
        self.fields['idTipoProducto'].label = 'Tipo de producto'


class inputTipoServicio(forms.ModelForm):
    class Meta:
        model = TipoServicio
        fields = ['nombre']

class inputServicio(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['nombre', 'precio', 'desc', 'idTipoServicio']
    def __init__(self, *args, **kwargs):
        super(inputServicio, self).__init__(*args, **kwargs)
        self.fields['desc'].label = 'Descripción'
        self.fields['idTipoServicio'].label = 'Tipo de servicio'

class inputCliente(forms.ModelForm):
    correo = forms.EmailField(label='Correo electrónico')
    class Meta:
        model = Cliente
        fields = ['identificacion', 'nombre', 'celular', 'correo', 'ciudad', 'direccion']
    def __init__(self, *args, **kwargs):
        super(inputCliente, self).__init__(*args, **kwargs)
        self.fields['identificacion'].label = 'Cédula de ciudadania'

class inputMoto(forms.ModelForm):
    class Meta:
        model = Moto
        fields = '__all__'

class inputOrden(forms.ModelForm):
    fecha_ingreso = forms.DateTimeField(label='Fecha de ingreso', widget=forms.TextInput (attrs={'value': datetime.today()}))
    desc_problema = forms.CharField(label='Descripción')
    info_adicional = forms.CharField(label='Información adicional')
    class Meta:
        model = OrdenDeIngreso
        fields = ['fecha_ingreso', 'desc_problema', 'info_adicional']