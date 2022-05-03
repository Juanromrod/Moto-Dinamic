from contextlib import redirect_stderr
from ctypes.wintypes import HLOCAL
from itertools import product
from django.shortcuts import render, redirect
from django.http import HttpResponse
import MotoDinamicApp

from MotoDinamicApp.models import Producto, Servicio, TipoProducto, TipoServicio
from .forms import inputProducto, inputServicio, inputTipoProducto, inputTipoServicio


def index(request):
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/login.html')

# Create your views here.
def insertarTipoProducto(request):
    if request.method == 'GET':
        form = inputTipoProducto()
        return render(request, 'MotoDinamicApp/creartipoProducto.html',{'form': form})
    elif request.method == 'POST':
        myTipoProducto = inputTipoProducto(request.POST)
        if myTipoProducto.is_valid():
            myTipoProducto.save()
        return redirect('insertar_tipoproducto')
    return HttpResponse("funcion insertar")

def insertarTipoServicio(request):
    if request.method == 'GET':
        form = inputTipoServicio()
        return render(request, 'MotoDinamicApp/creartipoServicio.html',{'form': form})
    elif request.method == 'POST':
        myTipoServicio = inputTipoServicio(request.POST)
        if myTipoServicio.is_valid():
            myTipoServicio.save()
        return redirect('insertar_tiposervicio')

def getTipoProducto(request):
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/searchTipoProducto.html')
    if request.method == 'POST':
        myId = request.POST['productId']
        myTipoProducto = TipoProducto.objects.get(id = myId)
        return HttpResponse(myTipoProducto.nombre)

def Productos(request):
    productos = Producto.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Productos.html', {'products': productos})
    if request.method == 'POST':
        myId = request.POST['productId']
        miProducto = Producto.objects.get(id = myId)
        return render(request, 'MotoDinamicApp/Productos.html', {'product': miProducto , 'products': productos})

def Servicios(request):
    servicios = Servicio.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Servicios.html', {'servicios': servicios})
    if request.method == 'POST':
        myId = request.POST['servicioId']
        miServicio = Servicio.objects.get(id = myId)
        return render(request, 'MotoDinamicApp/Servicios.html', {'servicio': miServicio , 'servicios': servicios})

def insertarProducto(request):
    if request.method == 'GET':
        form = inputProducto()
        return render(request, 'MotoDinamicApp/AgregarProductos.html',{'form': form})
    elif request.method == 'POST':
        myProducto = inputProducto(request.POST)
        if myProducto.is_valid():
            myProducto.save()
        return redirect('insertar_producto')

def insertarServicio(request):
    if request.method == 'GET':
        form = inputServicio()
        return render(request, 'MotoDinamicApp/AgregarServicios.html',{'form': form})
    elif request.method == 'POST':
        myServicio = inputServicio(request.POST)
        if myServicio.is_valid():
            myServicio.save()
        return redirect('insertar_servicio')

def modelimProducto(request):
    products = Producto.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/editarProducto.html', {'products': products})
    if request.method == 'POST':
        myId = request.POST['productId']
        miProducto = Producto.objects.get(id = myId)
        return render(request, 'MotoDinamicApp/editarProducto.html', {'product': miProducto , 'products': products})

def editarProducto(request, pk):
    producto = Producto.objects.get(id = pk)
    form = inputProducto(instance=producto)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/AgregarProductos.html', {'form': form})
    if request.method == 'POST':
        myProducto = inputProducto(request.POST, instance=producto)
        if myProducto.is_valid():
            myProducto.save()
        return redirect('editar_producto', pk)

def eliminarProducto(request, pk):
    producto = Producto.objects.get(id = pk)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/eliminarProducto.html', {'product': producto})
    if request.method == 'POST':
        producto.delete()
        return redirect('modelim_producto')

def modelimServicio(request):
    servicios = Servicio.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/editarServicio.html', {'servicios': servicios})
    if request.method == 'POST':
        myId = request.POST['servicioId']
        miServicio = Servicio.objects.get(id = myId)
        return render(request, 'MotoDinamicApp/editarServicio.html', {'servicio': miServicio , 'servicios': servicios})

def editarServicio(request, pk):
    servicio = Servicio.objects.get(id = pk)
    form = inputServicio(instance=servicio)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/AgregarServicios.html', {'form': form})
    if request.method == 'POST':
        miServicio = inputServicio(request.POST, instance=servicio)
        if miServicio.is_valid():
            miServicio.save()
        return redirect('editar_servicio', pk)

def eliminarServicio(request, pk):
    servicio = Servicio.objects.get(id = pk)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/eliminarServicio.html', {'servicio': servicio})
    if request.method == 'POST':
        servicio.delete()
        return redirect('modelim_servicio')