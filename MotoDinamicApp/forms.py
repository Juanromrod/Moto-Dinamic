from django import forms
from django.db import models
from django.db.models import fields
from .models import *

class inputTipoProducto(forms.ModelForm):
    class Meta:
        model = TipoProducto
        fields = ['nombre']


