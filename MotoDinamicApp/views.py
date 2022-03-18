from ctypes.wintypes import HLOCAL
from django.shortcuts import render
from django.http import HttpResponse

from MotoDinamicApp.models import TipoProducto


def index(request):
    return HttpResponse("Hola, Bienvenidos a Moto Dinamic.")
    

# Create your views here.
def insertarTipoProducto(request):
    tipoProducto = TipoProducto.objects.create(
        nombre = 'accesorio',
        desc = 'decoración'
    )
    tipoProducto.save()

    return HttpResponse("funcion insertar")