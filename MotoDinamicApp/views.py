from contextlib import redirect_stderr
from ctypes.wintypes import HLOCAL
from http import client
from itertools import product
from django.shortcuts import render, redirect
from django.http import HttpResponse
import MotoDinamicApp

from MotoDinamicApp.models import Cliente, Producto, Servicio, TipoProducto, Moto
from .forms import inputCliente, inputProducto, inputServicio, inputTipoProducto, inputTipoServicio, inputMoto


def index(request):
    return HttpResponse("Hola, Bienvenidos a Moto Dinamic.")

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

def insertarProducto(request):
    if request.method == 'GET':
        form = inputProducto()
        return render(request, 'MotoDinamicApp/AgregarProductos.html',{'form': form})
    elif request.method == 'POST':
        myProducto = inputProducto(request.POST)
        if myProducto.is_valid():
            myProducto.save()
        return redirect('insertar_producto')

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

def Servicios(request):
    servicios = Servicio.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Servicios.html', {'servicios': servicios})
    if request.method == 'POST':
        myId = request.POST['servicioId']
        miServicio = Servicio.objects.get(id = myId)
        return render(request, 'MotoDinamicApp/Servicios.html', {'servicio': miServicio , 'servicios': servicios})

def insertarServicio(request):
    if request.method == 'GET':
        form = inputServicio()
        return render(request, 'MotoDinamicApp/AgregarServicios.html',{'form': form})
    elif request.method == 'POST':
        myServicio = inputServicio(request.POST)
        if myServicio.is_valid():
            myServicio.save()
        return redirect('insertar_servicio')

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

def Clientes(request):
    clientes = Cliente.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Clientes.html', {'clientes': clientes})
    if request.method == 'POST':
        miId = request.POST['clienteId']
        miCliente = Cliente.objects.get(identificacion = miId)
        return render(request, 'MotoDinamicApp/Clientes.html', {'cliente': miCliente , 'clientes': clientes})

def insertarCliente(request):
    if request.method == 'GET':
        form = inputCliente()
        return render(request, 'MotoDinamicApp/AgregarClientes.html',{'form': form})
    elif request.method == 'POST':
        miCliente = inputCliente(request.POST)
        if miCliente.is_valid():
            miCliente.save()
        return redirect('insertar_cliente')

def modelimCliente(request):
    clientes = Cliente.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/editarCliente.html', {'clientes': clientes})
    if request.method == 'POST':
        miId = request.POST['clienteId']
        miCliente = Cliente.objects.get(identificacion = miId)
        return render(request, 'MotoDinamicApp/editarCliente.html', {'cliente': miCliente , 'clientes': clientes})

def editarCliente(request, pk):
    cliente = Cliente.objects.get(id = pk)
    form = inputCliente(instance=cliente)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/AgregarClientes.html', {'form': form})
    if request.method == 'POST':
        miCliente = inputCliente(request.POST, instance=cliente)
        if miCliente.is_valid():
            miCliente.save()
        return redirect('editar_cliente', pk)

def eliminarCliente(request, pk):
    cliente = Cliente.objects.get(id = pk)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/eliminarCliente.html', {'cliente': cliente})
    if request.method == 'POST':
        cliente.delete()
        return redirect('modelim_cliente')

def Motos(request):
    motos = Moto.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Motos.html', {'motos': motos})
    if request.method == 'POST':
        miId = request.POST['motoId']
        miMoto = Moto.objects.get(placa = miId)
        return render(request, 'MotoDinamicApp/Motos.html', {'moto': miMoto , 'motos': motos})

def insertarMoto(request):
    if request.method == 'GET':
        form = inputMoto()
        return render(request, 'MotoDinamicApp/AgregarMotos.html',{'form': form})
    elif request.method == 'POST':
        miMoto = inputMoto(request.POST)
        if miMoto.is_valid():
            miMoto.save()
        return redirect('insertar_moto')

def modelimMoto(request):
    motos = Moto.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/editarMoto.html', {'motos': motos})
    if request.method == 'POST':
        miId = request.POST['motoId']
        miMoto = Moto.objects.get(placa = miId)
        return render(request, 'MotoDinamicApp/editarMoto.html', {'moto': miMoto , 'motos': motos})

def editarMoto(request, pk):
    moto = Moto.objects.get(id = pk)
    form = inputMoto(instance=moto)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/AgregarMotos.html', {'form': form})
    if request.method == 'POST':
        miMoto = inputMoto(request.POST, instance=moto)
        if miMoto.is_valid():
            miMoto.save()
        return redirect('editar_moto', pk)

def eliminarMoto(request, pk):
    moto = Moto.objects.get(id = pk)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/eliminarMoto.html', {'moto': moto})
    if request.method == 'POST':
        moto.delete()
        return redirect('modelim_moto')