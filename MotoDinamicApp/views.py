from asyncio.windows_events import NULL
from contextlib import redirect_stderr
from ctypes.wintypes import HLOCAL
from http import client
from itertools import product
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .cart import Carrito
from MotoDinamicApp.models import Ciudad, Cliente, Producto, Servicio, TipoProducto, Moto
from .forms import inputCliente, inputProducto, inputServicio, inputTipoProducto, inputTipoServicio, inputMoto


# Create your views here.
def insertarTipoProducto(request):
    if request.method == 'GET':
        form = inputTipoProducto()
        return render(request, 'MotoDinamicApp/Productos/creartipoProducto.html',{'form': form})
    elif request.method == 'POST':
        myTipoProducto = inputTipoProducto(request.POST)
        if myTipoProducto.is_valid():
            myTipoProducto.save()
        return redirect('insertar_tipoproducto')
    return HttpResponse("funcion insertar")

def insertarTipoServicio(request):
    if request.method == 'GET':
        form = inputTipoServicio()
        return render(request, 'MotoDinamicApp/Servicios/creartipoServicio.html',{'form': form})
    elif request.method == 'POST':
        myTipoServicio = inputTipoServicio(request.POST)
        if myTipoServicio.is_valid():
            myTipoServicio.save()
        return redirect('insertar_tiposervicio')

def getTipoProducto(request):
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Productos/searchTipoProducto.html')
    if request.method == 'POST':
        myId = request.POST['productId']
        myTipoProducto = TipoProducto.objects.get(id = myId)
        return HttpResponse(myTipoProducto.nombre)

def Productos(request):
    carrito = Carrito(request)
    carrito.limpiar()
    productos = Producto.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Productos/Productos.html', {'products': productos})
    if request.method == 'POST':
        myId = request.POST['productId']
        miProducto = Producto.objects.get(id = myId)
        return render(request, 'MotoDinamicApp/Productos/Productos.html', {'product': miProducto , 'products': productos})

def insertarProducto(request):
    if request.method == 'GET':
        form = inputProducto()
        return render(request, 'MotoDinamicApp/Productos/AgregarProductos.html',{'form': form})
    elif request.method == 'POST':
        myProducto = inputProducto(request.POST)
        if myProducto.is_valid():
            myProducto.save()
        return redirect('insertar_producto')

def modelimProducto(request):
    products = Producto.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Productos/editarProducto.html', {'products': products})
    if request.method == 'POST':
        myId = request.POST['productId']
        miProducto = Producto.objects.get(id = myId)
        return render(request, 'MotoDinamicApp/Productos/editarProducto.html', {'product': miProducto , 'products': products})

def editarProducto(request, pk):
    producto = Producto.objects.get(id = pk)
    form = inputProducto(instance=producto)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/Productos/AgregarProductos.html', {'form': form})
    if request.method == 'POST':
        myProducto = inputProducto(request.POST, instance=producto)
        if myProducto.is_valid():
            myProducto.save()
        return redirect('editar_producto', pk)

def eliminarProducto(request, pk):
    producto = Producto.objects.get(id = pk)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/Productos/eliminarProducto.html', {'product': producto})
    if request.method == 'POST':
        producto.delete()
        return redirect('modelim_producto')

def Servicios(request):
    carrito = Carrito(request)
    carrito.limpiar()
    servicios = Servicio.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Servicios/Servicios.html', {'servicios': servicios})
    if request.method == 'POST':
        myId = request.POST['servicioId']
        miServicio = Servicio.objects.get(id = myId)
        return render(request, 'MotoDinamicApp/Servicios/Servicios.html', {'servicio': miServicio , 'servicios': servicios})

def insertarServicio(request):
    if request.method == 'GET':
        form = inputServicio()
        return render(request, 'MotoDinamicApp/Servicios/AgregarServicios.html',{'form': form})
    elif request.method == 'POST':
        myServicio = inputServicio(request.POST)
        if myServicio.is_valid():
            myServicio.save()
        return redirect('insertar_servicio')

def modelimServicio(request):
    servicios = Servicio.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Servicios/editarServicio.html', {'servicios': servicios})
    if request.method == 'POST':
        myId = request.POST['servicioId']
        miServicio = Servicio.objects.get(id = myId)
        return render(request, 'MotoDinamicApp/Servicios/editarServicio.html', {'servicio': miServicio , 'servicios': servicios})

def editarServicio(request, pk):
    servicio = Servicio.objects.get(id = pk)
    form = inputServicio(instance=servicio)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/Servicios/AgregarServicios.html', {'form': form})
    if request.method == 'POST':
        miServicio = inputServicio(request.POST, instance=servicio)
        if miServicio.is_valid():
            miServicio.save()
        return redirect('editar_servicio', pk)

def eliminarServicio(request, pk):
    servicio = Servicio.objects.get(id = pk)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/Servicios/eliminarServicio.html', {'servicio': servicio})
    if request.method == 'POST':
        servicio.delete()
        return redirect('modelim_servicio')

def Clientes(request):
    carrito = Carrito(request)
    carrito.limpiar()
    clientes = Cliente.objects.all()
    ciudades = ['Bogotá', 'Medellin', 'Cali', 'Barranquilla', 'Cartagena', 'Ibagué', 'Santa Marta', 'Manizales', 'Pereira', 'Neiva','Pasto', 'Armenia']
    if(len(Ciudad.objects.all()) == 0):
        for c in ciudades:
            ciudad = Ciudad.objects.create(nombre = c)
            ciudad.save()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Clientes/Clientes.html', {'clientes': clientes})
    if request.method == 'POST':
        miId = request.POST['clienteId']
        miCliente = Cliente.objects.get(identificacion = miId)
        return render(request, 'MotoDinamicApp/Clientes/Clientes.html', {'cliente': miCliente , 'clientes': clientes})

def insertarCliente(request):
    if request.method == 'GET':
        form = inputCliente()
        return render(request, 'MotoDinamicApp/Clientes/AgregarClientes.html',{'form': form})
    elif request.method == 'POST':
        miCliente = inputCliente(request.POST)
        if miCliente.is_valid():
            miCliente.save()
        return redirect('insertar_cliente')

def modelimCliente(request):
    clientes = Cliente.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Clientes/editarCliente.html', {'clientes': clientes})
    if request.method == 'POST':
        miId = request.POST['clienteId']
        miCliente = Cliente.objects.get(identificacion = miId)
        return render(request, 'MotoDinamicApp/Clientes/editarCliente.html', {'cliente': miCliente , 'clientes': clientes})

def editarCliente(request, pk):
    cliente = Cliente.objects.get(id = pk)
    form = inputCliente(instance=cliente)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/Clientes/AgregarClientes.html', {'form': form})
    if request.method == 'POST':
        miCliente = inputCliente(request.POST, instance=cliente)
        if miCliente.is_valid():
            miCliente.save()
        return redirect('editar_cliente', pk)

def eliminarCliente(request, pk):
    cliente = Cliente.objects.get(id = pk)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/Clientes/eliminarCliente.html', {'cliente': cliente})
    if request.method == 'POST':
        cliente.delete()
        return redirect('modelim_cliente')

def Motos(request):
    carrito = Carrito(request)
    carrito.limpiar()
    motos = Moto.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Motos/Motos.html', {'motos': motos})
    if request.method == 'POST':
        miId = request.POST['motoId']
        miMoto = Moto.objects.get(placa = miId)
        return render(request, 'MotoDinamicApp/Motos/Motos.html', {'moto': miMoto , 'motos': motos})

def insertarMoto(request):
    if request.method == 'GET':
        form = inputMoto()
        return render(request, 'MotoDinamicApp/Motos/AgregarMotos.html',{'form': form})
    elif request.method == 'POST':
        miMoto = inputMoto(request.POST)
        if miMoto.is_valid():
            miMoto.save()
        return redirect('insertar_moto')

def modelimMoto(request):
    motos = Moto.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Motos/editarMoto.html', {'motos': motos})
    if request.method == 'POST':
        miId = request.POST['motoId']
        miMoto = Moto.objects.get(placa = miId)
        return render(request, 'MotoDinamicApp/Motos/editarMoto.html', {'moto': miMoto , 'motos': motos})

def editarMoto(request, pk):
    moto = Moto.objects.get(id = pk)
    form = inputMoto(instance=moto)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/Motos/AgregarMotos.html', {'form': form})
    if request.method == 'POST':
        miMoto = inputMoto(request.POST, instance=moto)
        if miMoto.is_valid():
            miMoto.save()
        return redirect('editar_moto', pk)

def eliminarMoto(request, pk):
    moto = Moto.objects.get(id = pk)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/Motos/eliminarMoto.html', {'moto': moto})
    if request.method == 'POST':
        moto.delete()
        return redirect('modelim_moto')

def facturacionP(request):
    productos = Producto.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Facturacion/Productos.html', {'products': productos})
    if request.method == 'POST':
        myId = request.POST['productId']
        miProducto = Producto.objects.get(id = myId)
        return render(request, 'MotoDinamicApp/Facturacion/Productos.html', {'product': miProducto , 'products': productos})


def facturacionS(request):
    servicios = Servicio.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Facturacion/Servicios.html', {'servicios': servicios})
    if request.method == 'POST':
        myId = request.POST['servicioId']
        miServicio = Servicio.objects.get(id = myId)
        return render(request, 'MotoDinamicApp/Facturacion/Servicios.html', {'servicio': miServicio , 'servicios': servicios})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)
    carrito.agregarP(producto)
    return redirect('facturacion_p')

def agregar_servicio(request, servicio_id):
    carrito = Carrito(request)
    servicio = Servicio.objects.get(id = servicio_id)
    carrito.agregarS(servicio)
    return redirect('facturacion_s')

def aumentar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)
    carrito.agregarP(producto)
    return redirect('carrito')

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminarP(producto)
    return redirect('carrito')

def eliminar_servicio(request, servicio_id):
    carrito = Carrito(request)
    servicio = Servicio.objects.get(id=servicio_id)
    carrito.eliminarS(servicio)
    return redirect('carrito')

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect('carrito')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('facturacion_p')

def CarritoCompras(request):
    form = inputCliente()
    clientes = Cliente.objects.all()
    carrito = Carrito(request)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/Facturacion/Carrito.html', {'form': form})
    if request.method == 'POST':
        miId = request.POST['clienteId']
        miCliente = Cliente.objects.get(identificacion = miId)
        return render(request, 'MotoDinamicApp/Facturacion/Carrito.html', {'cliente': miCliente , 'clientes': clientes, 'form': form})
