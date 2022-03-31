from contextlib import redirect_stderr
from ctypes.wintypes import HLOCAL
from itertools import product
from django.shortcuts import render, redirect
from django.http import HttpResponse
import MotoDinamicApp

from MotoDinamicApp.models import Producto, TipoProducto
from .forms import inputProducto, inputTipoProducto


def index(request):
    return HttpResponse("Hola, Bienvenidos a Moto Dinamic.")

def insertTypeProduct(request):
    typeProduct = TipoProducto.objects.create(
        name = 'accesory',
        desc = 'This is an accesory for your moto'
    )

    typeProduct.save()
    return HttpResponse('test')

# Create your views here.
def insertarTipoProducto(request):
    if request.method == 'GET':
        form = inputTipoProducto()
        return render(request, 'MotoDinamicApp/creartipoProducto.html',{'form': form})
    elif request.method == 'POST':
        #print(myTipoProducto)
        myTipoProducto = inputTipoProducto(request.POST)
        if myTipoProducto.is_valid():
            myTipoProducto.save()
        return redirect('insertar')
    return HttpResponse("funcion insertar")

def getTipoProducto(request):
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/searchTipoProducto.html')
    if request.method == 'POST':
        myId = request.POST['productId']
        myTipoProducto = TipoProducto.objects.get(id = myId)
        return HttpResponse(myTipoProducto.nombre)

def Product(request):
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Productos.html')
    if request.method == 'POST':
        myId = request.POST['productId']
        miProducto = Producto.objects.get(id = myId)
        return render(request, 'MotoDinamicApp/Productos.html', {'product': miProducto})

def insertarProducto(request):
    if request.method == 'GET':
        form = inputProducto()
        return render(request, 'MotoDinamicApp/crearProducto.html',{'form': form})
    elif request.method == 'POST':
        myProducto = inputProducto(request.POST)
        if myProducto.is_valid():
            myProducto.save()
            producto = Producto.objects.get(id=1)
            print(producto.nombre)
        return redirect('insertar_producto')
    return HttpResponse("funcion insertar")