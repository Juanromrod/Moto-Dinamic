from xmlrpc.client import TRANSPORT_ERROR
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .cart import Carrito
from datetime import datetime
from django.contrib.auth.decorators import login_required
from MotoDinamicApp.models import Ciudad, Cliente, Cliente_Factura, Factura, Factura_Producto, Factura_Servicio, OrdenDeIngreso_Servicio, Producto, Servicio, TipoProducto, Moto, OrdenDeIngreso, TipoServicio
from .forms import inputCliente, inputProducto, inputServicio, inputTipoProducto, inputTipoServicio, inputMoto, inputOrden

# Create your views here.
@login_required(login_url='/')
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

@login_required(login_url='/')
def insertarTipoServicio(request):
    if request.method == 'GET':
        form = inputTipoServicio()
        return render(request, 'MotoDinamicApp/Servicios/creartipoServicio.html',{'form': form})
    elif request.method == 'POST':
        myTipoServicio = inputTipoServicio(request.POST)
        if myTipoServicio.is_valid():
            myTipoServicio.save()
        return redirect('insertar_tiposervicio')

@login_required(login_url='/')
def getTipoProducto(request):
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Productos/searchTipoProducto.html')
    if request.method == 'POST':
        myId = request.POST['productId']
        myTipoProducto = TipoProducto.objects.get(id = myId)
        return HttpResponse(myTipoProducto.nombre)

@login_required(login_url='/')
def Productos(request):
    carrito = Carrito(request)
    carrito.limpiar()
    productos = Producto.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Productos/Productos.html', {'products': productos})
    if request.method == 'POST':
        myId = request.POST['productId']
        try:
            miProducto = Producto.objects.get(id = myId)
            return render(request, 'MotoDinamicApp/Productos/Productos.html', {'product': miProducto , 'products': productos})
        except:
            n = True
            return render(request, 'MotoDinamicApp/Productos/Productos.html', {'products': productos, 'n': n})

@login_required(login_url='/')
def insertarProducto(request):
    tipos = ['Accesorio', 'Repuesto']
    if(len(TipoProducto.objects.all()) == 0):
        for p in tipos:
            tipo = TipoProducto.objects.create(nombre = p)
            tipo.save()
    if request.method == 'GET':
        form = inputProducto()
        return render(request, 'MotoDinamicApp/Productos/AgregarProductos.html',{'form': form})
    elif request.method == 'POST':
        myProducto = inputProducto(request.POST, request.FILES)
        if myProducto.is_valid():
            myProducto.save()
        return redirect('insertar_producto')

@login_required(login_url='/')
def modelimProducto(request):
    products = Producto.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Productos/editarProducto.html', {'products': products})
    if request.method == 'POST':
        myId = request.POST['productId']
        try:
            miProducto = Producto.objects.get(id = myId)
            return render(request, 'MotoDinamicApp/Productos/editarProducto.html', {'product': miProducto , 'products': products})
        except:
            n = True
            return render(request, 'MotoDinamicApp/Productos/editarProducto.html', {'products': products, 'n': n})

@login_required(login_url='/')
def editarProducto(request, pk):
    producto = Producto.objects.get(id = pk)
    form = inputProducto(instance=producto)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/Productos/AgregarProductos.html', {'form': form})
    if request.method == 'POST':
        myProducto = inputProducto(request.POST, request.FILES, instance=producto)
        if myProducto.is_valid():
            myProducto.save()
        return redirect('editar_producto', pk)

@login_required(login_url='/')
def eliminarProducto(request, pk):
    producto = Producto.objects.get(id = pk)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/Productos/eliminarProducto.html', {'product': producto})
    if request.method == 'POST':
        producto.delete()
        return redirect('modelim_producto')

@login_required(login_url='/')
def Servicios(request):
    carrito = Carrito(request)
    carrito.limpiar()
    servicios = Servicio.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Servicios/Servicios.html', {'servicios': servicios})
    if request.method == 'POST':
        myId = request.POST['servicioId']
        try:
            miServicio = Servicio.objects.get(id = myId)
            return render(request, 'MotoDinamicApp/Servicios/Servicios.html', {'servicio': miServicio , 'servicios': servicios})
        except:
            n = True
            return render(request, 'MotoDinamicApp/Servicios/Servicios.html', {'servicios': servicios, 'n': n})

@login_required(login_url='/')
def insertarServicio(request):
    tipos = ['Limpieza', 'Revisión', 'Arreglo']
    if(len(TipoServicio.objects.all()) == 0):
        for p in tipos:
            tipo = TipoServicio.objects.create(nombre = p)
            tipo.save()
    if request.method == 'GET':
        form = inputServicio()
        return render(request, 'MotoDinamicApp/Servicios/AgregarServicios.html',{'form': form})
    elif request.method == 'POST':
        myServicio = inputServicio(request.POST)
        if myServicio.is_valid():
            myServicio.save()
        return redirect('insertar_servicio')

@login_required(login_url='/')
def modelimServicio(request):
    servicios = Servicio.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Servicios/editarServicio.html', {'servicios': servicios})
    if request.method == 'POST':
        myId = request.POST['servicioId']
        try:
            miServicio = Servicio.objects.get(id = myId)
            return render(request, 'MotoDinamicApp/Servicios/editarServicio.html', {'servicio': miServicio , 'servicios': servicios})
        except:
            n = True
            return render(request, 'MotoDinamicApp/Servicios/editarServicio.html', {'servicios': servicios, 'n': n})

@login_required(login_url='/')
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

@login_required(login_url='/')
def eliminarServicio(request, pk):
    servicio = Servicio.objects.get(id = pk)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/Servicios/eliminarServicio.html', {'servicio': servicio})
    if request.method == 'POST':
        servicio.delete()
        return redirect('modelim_servicio')

@login_required(login_url='/')
def Clientes(request):
    carrito = Carrito(request)
    carrito.limpiar()
    clientes = Cliente.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Clientes/Clientes.html', {'clientes': clientes})
    if request.method == 'POST':
        miId = request.POST['clienteId']
        try:
            miCliente = Cliente.objects.get(identificacion = miId)
            return render(request, 'MotoDinamicApp/Clientes/Clientes.html', {'cliente': miCliente , 'clientes': clientes})
        except:
            n = True
            return render(request, 'MotoDinamicApp/Clientes/Clientes.html', {'clientes': clientes, 'n': n})
@login_required(login_url='/')
def insertarCliente(request):
    form = inputCliente()
    ciudades = ['Bogotá', 'Medellin', 'Cali', 'Barranquilla', 'Cartagena', 'Ibagué', 'Santa Marta', 'Manizales', 'Pereira', 'Neiva','Pasto', 'Armenia']
    if(len(Ciudad.objects.all()) == 0):
        for c in ciudades:
            ciudad = Ciudad.objects.create(nombre = c)
            ciudad.save()
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/Clientes/AgregarClientes.html',{'form': form})
    elif request.method == 'POST':
        miCliente = inputCliente(request.POST)
        if miCliente.is_valid():
            miCliente.save()
            return redirect('insertar_cliente')
        else:
            n = True
            return render(request, 'MotoDinamicApp/Clientes/AgregarClientes.html',{'form': form, 'n':n})

@login_required(login_url='/')
def modelimCliente(request):
    clientes = Cliente.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Clientes/editarCliente.html', {'clientes': clientes})
    if request.method == 'POST':
        miId = request.POST['clienteId']
        try:
            miCliente = Cliente.objects.get(identificacion = miId)
            return render(request, 'MotoDinamicApp/Clientes/editarCliente.html', {'cliente': miCliente , 'clientes': clientes})
        except:
            n = True
            return render(request, 'MotoDinamicApp/Clientes/editarCliente.html', {'clientes': clientes, 'n': n})

@login_required(login_url='/')
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

@login_required(login_url='/')
def eliminarCliente(request, pk):
    cliente = Cliente.objects.get(id = pk)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/Clientes/eliminarCliente.html', {'cliente': cliente})
    if request.method == 'POST':
        cliente.delete()
        return redirect('modelim_cliente')

@login_required(login_url='/')
def Motos(request):
    carrito = Carrito(request)
    carrito.limpiar()
    motos = Moto.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Motos/Motos.html', {'motos': motos})
    if request.method == 'POST':
        miId = request.POST['motoId']
        try:
            miMoto = Moto.objects.get(placa = miId)
            return render(request, 'MotoDinamicApp/Motos/Motos.html', {'moto': miMoto , 'motos': motos})
        except:
            n = True
            return render(request, 'MotoDinamicApp/Motos/Motos.html', {'motos': motos, 'n':n})

@login_required(login_url='/')
def insertarMoto(request):
    form = inputMoto()
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/Motos/AgregarMotos.html',{'form': form})
    elif request.method == 'POST':
        miMoto = inputMoto(request.POST, request.FILES)
        if miMoto.is_valid():
            miMoto.save()
            return redirect('insertar_moto')
        else:
            n = True
            return render(request, 'MotoDinamicApp/Motos/AgregarMotos.html',{'form': form, 'n': n})

@login_required(login_url='/')
def modelimMoto(request):
    motos = Moto.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Motos/editarMoto.html', {'motos': motos})
    if request.method == 'POST':
        miId = request.POST['motoId']
        try:
            miMoto = Moto.objects.get(placa = miId)
            return render(request, 'MotoDinamicApp/Motos/editarMoto.html', {'moto': miMoto , 'motos': motos})
        except:
            n = True
            return render(request, 'MotoDinamicApp/Motos/editarMoto.html', {'motos': motos, 'n': n})

@login_required(login_url='/')
def editarMoto(request, pk):
    moto = Moto.objects.get(id = pk)
    form = inputMoto(instance=moto)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/Motos/AgregarMotos.html', {'form': form})
    if request.method == 'POST':
        miMoto = inputMoto(request.POST, request.FILES, instance=moto)
        if miMoto.is_valid():
            miMoto.save()
        return redirect('editar_moto', pk)

@login_required(login_url='/')
def eliminarMoto(request, pk):
    moto = Moto.objects.get(id = pk)
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/Motos/eliminarMoto.html', {'moto': moto})
    if request.method == 'POST':
        moto.delete()
        return redirect('modelim_moto')

@login_required(login_url='/')
def facturacionP(request):
    productos = Producto.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Facturacion/Productos.html', {'products': productos})
    if request.method == 'POST':
        myId = request.POST['productId']
        try:
            miProducto = Producto.objects.get(id = myId)
            return render(request, 'MotoDinamicApp/Facturacion/Productos.html', {'product': miProducto , 'products': productos})
        except:
            n = True
            return render(request, 'MotoDinamicApp/Facturacion/Productos.html', {'products': productos, 'n':n})

@login_required(login_url='/')
def facturacionS(request):
    servicios = Servicio.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Facturacion/Servicios.html', {'servicios': servicios})
    if request.method == 'POST':
        myId = request.POST['servicioId']
        try:
            miServicio = Servicio.objects.get(id = myId)
            return render(request, 'MotoDinamicApp/Facturacion/Servicios.html', {'servicio': miServicio , 'servicios': servicios})
        except:
            n = True
            return render(request, 'MotoDinamicApp/Facturacion/Servicios.html', {'servicios': servicios, 'n':n})

@login_required(login_url='/')
def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)
    carrito.agregarP(producto)
    return redirect('facturacion_p')

@login_required(login_url='/')
def agregar_servicio(request, servicio_id):
    carrito = Carrito(request)
    servicio = Servicio.objects.get(id = servicio_id)
    carrito.agregarS(servicio)
    return redirect('facturacion_s')

@login_required(login_url='/')
def aumentar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)
    carrito.agregarP(producto)
    return redirect('carrito')

@login_required(login_url='/')
def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminarP(producto)
    return redirect('carrito')

@login_required(login_url='/')
def eliminar_servicio(request, servicio_id):
    carrito = Carrito(request)
    servicio = Servicio.objects.get(id=servicio_id)
    carrito.eliminarS(servicio)
    return redirect('carrito')

@login_required(login_url='/')
def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect('carrito')

@login_required(login_url='/')
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect('facturacion_p')

@login_required(login_url='/')
def CarritoCompras(request):
    ciudades = ['Bogotá', 'Medellin', 'Cali', 'Barranquilla', 'Cartagena', 'Ibagué', 'Santa Marta', 'Manizales', 'Pereira', 'Neiva','Pasto', 'Armenia']
    if(len(Ciudad.objects.all()) == 0):
        for c in ciudades:
            ciudad = Ciudad.objects.create(nombre = c)
            ciudad.save()
    clienteform = inputCliente()
    clientes = Cliente.objects.all()
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/Facturacion/Carrito.html', {'clienteform': clienteform})
    if request.method == 'POST':
        miId = request.POST['clienteId']
        try:
            miCliente = Cliente.objects.get(identificacion = miId)
            return render(request, 'MotoDinamicApp/Facturacion/Carrito.html', {'cliente': miCliente , 'clientes': clientes, 'clienteform': clienteform})
        except:
            n = True
            return render(request, 'MotoDinamicApp/Facturacion/Carrito.html', {'clienteform': clienteform, 'n':n})

@login_required(login_url='/')
def buscarCliente(request):
    clienteform = inputCliente()
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/Facturacion/Carrito.html',{'clienteform': clienteform})
    if request.method == 'POST':
        miId = request.POST['clienteId']
        try:
            miCliente = Cliente.objects.get(identificacion = miId)
            return render(request, 'MotoDinamicApp/Facturacion/Carrito.html', {'cliente': miCliente,'clienteform': clienteform})
        except:
            n = True
            return render(request, 'MotoDinamicApp/Facturacion/Carrito.html',{'clienteform': clienteform, 'n':n})

@login_required(login_url='/')
def crearCliente(request):
    clienteform = inputCliente()
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/Facturacion/Carrito.html',{'clienteform': clienteform})
    elif request.method == 'POST':
        cliente = inputCliente(request.POST)
        miId = request.POST['identificacion']
        if(cliente.is_valid()):
            cliente.save()
            miCliente = Cliente.objects.get(identificacion = miId)
            return render(request, 'MotoDinamicApp/Facturacion/Carrito.html', {'cliente': miCliente, 'clienteform': clienteform})
        else:
            nt = True
            return render(request, 'MotoDinamicApp/Facturacion/Carrito.html',{'clienteform': clienteform, 'nt':nt})


@login_required(login_url='/')
def facturas(request):
    c_f = Cliente_Factura.objects.all()
    facturas = Factura.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Facturacion/Facturas.html', {'facturas': facturas, 'c_f': c_f})
    if request.method == 'POST':
        myId = request.POST['facturaId']
        try:
            miFactura = Factura.objects.get(id = myId)
            return render(request, 'MotoDinamicApp/Facturacion/Facturas.html', {'miFactura': miFactura, 'facturas': facturas, 'c_f': c_f})
        except:
            n = True
            return render(request, 'MotoDinamicApp/Facturacion/Facturas.html', {'facturas': facturas, 'c_f': c_f, 'n': n})


@login_required(login_url='/')
def verFactura(request, miFactura):
    c_f = Cliente_Factura.objects.get(idFactura = miFactura)
    f_p = Factura_Producto.objects.filter(idFactura = miFactura)
    f_s = Factura_Servicio.objects.filter(idFactura = miFactura)
    miFactura = Factura.objects.get(id = miFactura)
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Facturacion/VerFactura.html', {'miFactura': miFactura, 'c_f': c_f, 'f_p': f_p, 'f_s': f_s})

@login_required(login_url='/')
def insertarFactura(request, cliente_id, eltotal):
    cliente = Cliente.objects.get(id = cliente_id)
    carrito = Carrito(request)
    iva = carrito.getIva()
    if request.method == 'GET':
        lafecha = datetime.today()
        miFactura = Factura.objects.create(fecha = lafecha, iva = iva, total = eltotal)
        cliente = Cliente.objects.get(id = cliente_id)
        Cliente_Factura.objects.create(idCliente = cliente, idFactura = miFactura)
        idservicios = carrito.getServicios()
        idproductos = carrito.getProductos()
        cantidad = carrito.getCantidad()
        cont = 0
        for idp in idproductos:
            producto = Producto.objects.get(id = idp)
            producto.stock -= cantidad[cont]
            producto.save()
            Factura_Producto.objects.create(idProducto = producto, cantidad = cantidad[cont], idFactura = miFactura)
            cont += 1
        for ids in idservicios:
            servicio = Servicio.objects.get(id = ids)
            Factura_Servicio.objects.create(idservicio = servicio, idFactura = miFactura)
        carrito = Carrito(request)
        carrito.limpiar()
        return redirect('facturas')

@login_required(login_url='/')
def ordenes(request):
    o_s = OrdenDeIngreso_Servicio.objects.all()
    ordenes = OrdenDeIngreso.objects.all()
    if request.method == "GET":
        return render(request, 'MotoDinamicApp/Ordenes/Ordenes.html', {'ordenes': ordenes, 'o_s': o_s})
    if request.method == 'POST':
        myId = request.POST['ordenId']
        miMoto = Moto.objects.get(placa = myId)
        misOrdenes = OrdenDeIngreso.objects.filter(idMoto = miMoto.id)
        return render(request, 'MotoDinamicApp/Ordenes/Ordenes.html', {'misOrdenes': misOrdenes , 'ordenes': ordenes, 'o_s': o_s})

@login_required(login_url='/')
def insertarOrden(request, miplaca, cliente_id, eltotal):
    cliente = Cliente.objects.get(id = cliente_id)
    carrito = Carrito(request)
    iva = carrito.getIva()
    idservicios = carrito.getServicios()
    idproductos = carrito.getProductos()
    cantidad = carrito.getCantidad()
    if request.method == 'POST':
        fecha = request.POST['fecha_ingreso']
        desc = request.POST['desc_problema']
        info = request.POST['info_adicional']
        miMoto = Moto.objects.get(placa = miplaca)
        miOrden = OrdenDeIngreso.objects.create(idMoto = miMoto, desc_problema = desc, fecha_ingreso = fecha, info_adicional = info)
        for ids in idservicios:
            miServicio = Servicio.objects.get(id = ids)
            OrdenDeIngreso_Servicio.objects.create(idOrdenDeIngreso = miOrden, idServicio = miServicio)
        lafecha = datetime.today()
        miFactura = Factura.objects.create(fecha = lafecha, iva = iva, total = eltotal)
        cliente = Cliente.objects.get(id = cliente_id)
        Cliente_Factura.objects.create(idCliente = cliente, idFactura = miFactura)
        for idp in idproductos:
            cont = 0
            producto = Producto.objects.get(id = idp)
            producto.stock -= cantidad[cont]
            producto.save()
            Factura_Producto.objects.create(idProducto = producto, cantidad = cantidad[cont], idFactura = miFactura)
            cont += 1
        for ids in idservicios:
            servicio = Servicio.objects.get(id = ids)
            Factura_Servicio.objects.create(idServicio = servicio, idFactura = miFactura)
        carrito = Carrito(request)
        carrito.limpiar()
        return redirect('ordenes')

@login_required(login_url='/')
def buscarMoto(request, cliente_id, eltotal):
    orderform = inputOrden()
    motoform = inputMoto()
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/Ordenes/AgregarOrdenes.html',{'orderform': orderform, 'motoform': motoform, 'clienteid': cliente_id, 'total': eltotal})
    elif request.method == 'POST':
        miId = request.POST['motoId']
        try:
            miMoto = Moto.objects.get(placa = miId)
            return render(request, 'MotoDinamicApp/Ordenes/AgregarOrdenes.html',{'orderform': orderform, 'motoform': motoform, 'moto': miMoto, 'clienteid': cliente_id, 'total': eltotal})
        except:
            n = True
            return render(request, 'MotoDinamicApp/Ordenes/AgregarOrdenes.html',{'orderform': orderform, 'motoform': motoform, 'clienteid': cliente_id, 'total': eltotal, 'n':n})

@login_required(login_url='/')
def crearMoto(request, cliente_id, eltotal):
    orderform = inputOrden()
    motoform = inputMoto()
    if request.method == 'GET':
        return render(request, 'MotoDinamicApp/Ordenes/AgregarOrdenes.html',{'orderform': orderform, 'motoform': motoform, 'clienteid': cliente_id, 'total': eltotal})
    elif request.method == 'POST':
        moto = inputMoto(request.POST)
        miplaca = request.POST['placa']
        if(moto.is_valid()):
            moto.save()
            miMoto = Moto.objects.get(placa = miplaca)
            return render(request, 'MotoDinamicApp/Ordenes/AgregarOrdenes.html',{'orderform': orderform, 'motoform': motoform, 'moto': miMoto, 'clienteid': cliente_id, 'total': eltotal})
        else:
            nt=True
            return render(request, 'MotoDinamicApp/Ordenes/AgregarOrdenes.html',{'orderform': orderform, 'motoform': motoform, 'clienteid': cliente_id, 'total': eltotal, 'nt':nt})