from xml.dom.minidom import Document
from django.urls import path
from . import views

urlpatterns = [
    path('tipoproducto/', views.insertarTipoProducto, name='insertar_tipoproducto'),
    path('vertipoproducto/', views.getTipoProducto, name='get_producto'),
    path('crearproducto/', views.insertarProducto, name='insertar_producto'),
    path('productos/', views.Productos, name='productos'),
    path('editarproducto/', views.modelimProducto, name='modelim_producto'),
    path('editarP/<str:pk>/', views.editarProducto, name='editar_producto'),
    path('eliminarP/<str:pk>/', views.eliminarProducto, name='eliminar_producto'),
    path('tiposervicio/', views.insertarTipoServicio, name='insertar_tiposervicio'),
    path('crearservicio/', views.insertarServicio, name='insertar_servicio'),
    path('servicios/', views.Servicios, name='servicios'),
    path('editarservicio/', views.modelimServicio, name='modelim_servicio'),
    path('editarS/<str:pk>/', views.editarServicio, name='editar_servicio'),
    path('eliminarS/<str:pk>/', views.eliminarServicio, name='eliminar_servicio'),
    path('clientes/', views.Clientes, name='clientes'),
    path('crearcliente/', views.insertarCliente, name='insertar_cliente'),
    path('editarcliente/', views.modelimCliente, name='modelim_cliente'),
    path('editarC/<str:pk>/', views.editarCliente, name='editar_cliente'),
    path('eliminarC/<str:pk>/', views.eliminarCliente, name='eliminar_cliente'),
    path('motos/', views.Motos, name='motos'),
    path('crearmoto/', views.insertarMoto, name='insertar_moto'),
    path('editarmoto/', views.modelimMoto, name='modelim_moto'),
    path('editarM/<str:pk>/', views.editarMoto, name='editar_moto'),
    path('eliminarM/<str:pk>/', views.eliminarMoto, name='eliminar_moto'),
    path('facturarproductos/', views.facturacionP, name='facturacion_p'),
    path('facturarservicios/', views.facturacionS, name='facturacion_s'),
    path('agregarP/<int:producto_id>/', views.agregar_producto, name='añadir_producto'),
    path('agregarS/<int:servicio_id>/', views.agregar_servicio, name='añadir_servicio'),
    path('aumentarP/<int:producto_id>/', views.aumentar_producto, name='aumentar_producto'),
    path('eliminarPC/<int:producto_id>/', views.eliminar_producto, name="elim_producto"),
    path('eliminarSC/<int:servicio_id>/', views.eliminar_servicio, name="elim_servicio"),
    path('restar/<int:producto_id>/', views.restar_producto, name="restar_producto"),
    path('limpiar/', views.limpiar_carrito, name="limpiar_carrito"),
    path('carrito/', views.CarritoCompras, name='carrito'),
    path('ordenes/', views.ordenes, name='ordenes'),
    path('crearorden/<str:cliente_id>/<int:eltotal>/', views.buscarMoto, name='insertar_orden'),
    path('completarorden/<str:miplaca>/<str:cliente_id>/<int:eltotal>/', views.insertarOrden, name='completar_orden'),
    path('añadirmoto/<str:cliente_id>/<int:eltotal>/', views.crearMoto, name='añadir_moto'),
    path('buscarcliente/', views.buscarCliente, name='buscar_cliente'),
    path('añadircliente/', views.crearCliente, name='añadir_cliente'),
    path('completarfactura/<str:cliente_id>/<int:eltotal>/', views.insertarFactura, name='completar_factura'),
    path('win/', views.selogro, name='win'),
]