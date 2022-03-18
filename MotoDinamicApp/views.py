from ctypes.wintypes import HLOCAL
from django.shortcuts import render
from django.http import HttpResponse

from MotoDinamicApp.models import TypeProduct


def index(request):
    return HttpResponse("Hola, Bienvenidos a Moto Dinamic.")

def insertTypeProduct(request):
    typeProduct = TypeProduct.objects.create(
        name = 'accesory',
        desc = 'This is an accesory for your moto'
    )

    typeProduct.save()
    return HttpResponse('test')

# Create your views here.
