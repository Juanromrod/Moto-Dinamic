from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
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
]